from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
from clip_interrogator import Config, Interrogator
import requests

app = Flask(__name__)



ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))

@app.route('/')
def example():
    url = request.args.get('url')
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert('RGB')
        return ci.interrogate(img)
    except Exception as e:   # 捕获所有Exception类及其子类抛出的异常/errors 
        return e

if __name__ == '__main__':
 app.run(debug=True, port=8083)