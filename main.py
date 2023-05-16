from flask import Flask, request
from PIL import Image
from io import BytesIO
from clip_interrogator import Config, Interrogator
import requests

ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))
Image.open("./1.jpg").convert('RGB')
app = Flask(__name__)

@app.route('/')
def ImageToDescription():
    url = request.args.get('url')
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert('RGB')
        ci.interrogate(img)
        return "done"
    except Exception as e:   # 捕获所有Exception类及其子类抛出的异常/errors 
        return e

if __name__ == '__main__':
 app.run(debug=True, port=8083)