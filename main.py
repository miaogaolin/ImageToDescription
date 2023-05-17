from flask import Flask, request
from PIL import Image
from io import BytesIO
from clip_interrogator import Config, Interrogator
import requests

ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))

app = Flask(__name__)

@app.route('/')
def ImageToDescription():
    url = request.args.get('url')
    mode = request.args.get('mode')
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert('RGB')
    
    if mode == 'classic':
       return ci.interrogate_classic(img)
    elif mode == 'negative':
       return ci.interrogate_negative(img)
       
    return ci.interrogate_fast(img)
   

if __name__ == '__main__':
 app.run(debug=True, port=8083, host='0.0.0.0')