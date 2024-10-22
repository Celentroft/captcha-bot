import json
import random
from typing import Dict, Any
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io

def load_json() -> Dict[str, Any]:
    config = json.load(open("config.json", 'r'))
    return config

def embed_color() -> int:
    config = load_json()
    return int(config['color'], 16)

def gen_captcha(code):
    img = Image.new('RGB', (600, 200), color=(255, 255, 255))  
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 50)  
    except IOError:
        font = ImageFont.load_default()  
    x_start = 20
    for char in code:
        angle = random.randint(-30, 30)
        char_font_size = random.randint(40, 70)
        font = ImageFont.truetype("arial.ttf", char_font_size)
        char_img = Image.new('RGBA', (80, 80), color=(255, 255, 255, 0)) 
        char_draw = ImageDraw.Draw(char_img)
        char_draw.text((10, 10), char, font=font, fill=(0, 0, 0))
        char_img = char_img.rotate(angle, expand=1)
        img.paste(char_img, (x_start, random.randint(30, 70)), char_img)  
        x_start += char_font_size + random.randint(5, 15)
    for _ in range(5):
        start_point = (random.randint(0, 600), random.randint(0, 200))
        end_point = (random.randint(0, 600), random.randint(0, 200))
        d.line([start_point, end_point], fill=(0, 0, 0), width=2)
    img = img.filter(ImageFilter.GaussianBlur(1))
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf