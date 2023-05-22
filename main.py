from flask import Flask, request
from PIL import Image
from io import BytesIO
from clip_interrogator import Config, Interrogator
import requests
import oss2
import yaml
import datetime
import os
import threading

ci = Interrogator(Config(clip_model_name="ViT-L-14/openai",chunk_size=13312))

app = Flask(__name__)


@app.route('/')
def ImageToDescription():
    try:
        url = request.args.get('url')
        mode = request.args.get('mode')
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert('RGB')
        
        if mode == 'classic':
            return ci.interrogate_classic(img)
        elif mode == 'negative':
            return ci.interrogate_negative(img)
        elif mode == 'best':
            return ci.interrogate(img)
        return ci.interrogate_fast(img)
    except  Exception as e:
       return str(e);
   

maxImageCount = 10
def GetOssImages(bucket, mode, dealCount=0, prefix=''):
  if dealCount >= maxImageCount: 
    return
  for obj in oss2.ObjectIteratorV2(bucket,prefix=prefix):
        if dealCount >= maxImageCount: 
            return
        pname=obj.key.replace(prefix,'',1).lstrip('/')
        name=f"{prefix}/{pname}" if prefix else pname 
        if obj.is_prefix():
            GetOssImages(bucket,mode, dealCount, name)
        elif name.endswith(('.jpg','.jpeg','.bmp','.gif','.png', '.webp')):
            # 只处理这样的图片 623af516ba10f659170849.jpg
            if len(getFileBasename(name)) != 22:
                return
            
            imgContent = bucket.get_object(name).read()
            img = Image.open(BytesIO(imgContent)).convert('RGB')
            
            with open(mode+'.csv', mode='a+', encoding='utf-8') as f:
                des = ''
                if mode == 'classic':
                    des = ci.interrogate_classic(img)
                elif mode == 'negative':
                    des = ci.interrogate_negative(img)
                elif mode == 'best':
                    des = ci.interrogate(img)
                elif mode == 'fast':
                    des = ci.interrogate_fast(img)

                now = datetime.datetime.now()
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")

                filename =  os.path.basename(name)
                dealCount += 1
                f.write(current_time + ',' +filename+','+des + '\n')
                


threads = []
def ConcurrenceModel(bucket, mode, dealCount=0, prefix=''):
    if dealCount >= maxImageCount: 
        return
    for obj in oss2.ObjectIteratorV2(bucket,prefix=prefix):
        if dealCount >= maxImageCount: 
            return
        pname=obj.key.replace(prefix,'',1).lstrip('/')
        name=f"{prefix}/{pname}" if prefix else pname 
        if obj.is_prefix():
            ConcurrenceModel(bucket,mode, dealCount, name)
        elif name.endswith(('.jpg','.jpeg','.bmp','.gif','.png', '.webp')):
            # 只处理这样的图片 623af516ba10f659170849.jpg
            if len(getFileBasename(name)) != 22:
                return
            
            t = threading.Thread(target=concurrenceSub(mode, name))
            threads.append(t)
            t.start()

            if len(threads) >= 5:
                for t in threads:
                    t.join()
                

def concurrenceSub(mode, name):
    imgContent = bucket.get_object(name).read()
    img = Image.open(BytesIO(imgContent)).convert('RGB')
    
    with open(mode+'.csv', mode='a+', encoding='utf-8') as f:
        des = ''
        if mode == 'classic':
            des = ci.interrogate_classic(img)
        elif mode == 'negative':
            des = ci.interrogate_negative(img)
        elif mode == 'best':
            des = ci.interrogate(img)
        elif mode == 'fast':
            des = ci.interrogate_fast(img)

        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        filename =  os.path.basename(name)
        dealCount += 1
        f.write(current_time + ',' +filename+','+des + '\n')
                    

def getFileBasename(filepath):
    filename_with_extension = os.path.basename(filepath) # 获取带有后缀的完整文件名称: myfile.txt
    filename_without_extension = os.path.splitext(filename_with_extension)[0] # 删除扩展名：myfile
    return filename_without_extension
    
if __name__ == '__main__':
    # app.run(debug=True, port=8083, host='0.0.0.0')
    with open('conf.yaml', 'r') as f:
        data = yaml.safe_load(f)
        access_key_id = data['alioss']['accessKeyId']     # 替换为您的 access key id.
        access_key_secret = data['alioss']['accessKeySecret']   # 替换为您的 access key secret.
        # 对于公共访问，请设置endpoint：
        bucket_name, endpoint = data['alioss']['bucket'],data['alioss']['endpoint']    # 填写自己在控制台上创建存储空间时指定的名字和地区域名。
        auth = oss2.Auth(access_key_id, access_key_secret)
        bucket = oss2.Bucket(auth, endpoint, bucket_name)
        print('start fast model, time:',datetime.datetime.now())
        GetOssImages(bucket, 'fast')
        print('end fast model, time:',datetime.datetime.now())

        print('start classic model, time:',datetime.datetime.now())
        GetOssImages(bucket, 'classic')
        print('end classic model, time:',datetime.datetime.now())

        print('start best model, time:',datetime.datetime.now())
        ConcurrenceModel(bucket, 'best')
        for t in threads:
            t.join()
        print('end best model, time:',datetime.datetime.now())
    