import random

from PIL import Image,ImageDraw,ImageFont
from io import BytesIO

def get_vaild_code():
    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    img = Image.new("RGB", (270, 40), color='grey')
    font = ImageFont.truetype("static/font/kumo.ttf", size=40)
    draw = ImageDraw.Draw(img)
    width = 270
    height = 35
    valid_code = ""
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(97, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        valid_code += char
        draw.text((50 * i + 20, 0), char, 'blue', font=font)
    f = BytesIO()
    img.save(f, 'png')
    data = f.getvalue()
    return data, valid_code


