from flask import Flask, request
from PIL import Image
from io import BytesIO
from clip_interrogator import Config, Interrogator
import requests
import oss2
import yaml
import datetime

ci = Interrogator(Config(clip_model_name="ViT-L-14/openai",chunk_size=10240, caption_max_length=64))

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
   

def GetOssImages(bucket, prefix=''):
  for obj in oss2.ObjectIteratorV2(bucket,prefix=prefix):
        pname=obj.key.replace(prefix,'',1).lstrip('/')
        name=f"{prefix}/{pname}" if prefix else pname 
        if obj.is_prefix():
            GetOssImages(bucket,name)
        elif name.endswith(('.jpg','.jpeg','.bmp','.gif','.png', '.webp')):
            imgContent = bucket.get_object(name).read()
            img = Image.open(BytesIO(imgContent)).convert('RGB')
            
            with open('image_des.csv', mode='a+', encoding='utf-8') as f:
                des = ci.interrogate_fast(img)
                now = datetime.datetime.now()
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                f.write(current_time + ',' +name+','+des + '\n')
   
if __name__ == '__main__':
    app.run(debug=True, port=8083, host='0.0.0.0')
    with open('conf.yaml', 'r') as f:
        data = yaml.safe_load(f)
        access_key_id = data['alioss']['accessKeyId']     # 替换为您的 access key id.
        access_key_secret = data['alioss']['accessKeySecret']   # 替换为您的 access key secret.
        # 对于公共访问，请设置endpoint：
        bucket_name, endpoint = data['alioss']['bucket'],data['alioss']['endpoint']    # 填写自己在控制台上创建存储空间时指定的名字和地区域名。
        auth = oss2.Auth(access_key_id, access_key_secret)
        bucket = oss2.Bucket(auth, endpoint, bucket_name) 
        GetOssImages(bucket)
    