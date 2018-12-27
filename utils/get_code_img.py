# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : wuyifei
# Data    : 12/27/18 1:51 PM
# FileName: get_code_img.py
from django.shortcuts import HttpResponse
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import random

def get_code(request):
    img = Image.new(mode="RGB",size=(120,40),color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    draw = ImageDraw.Draw(img,"RGB")
    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, 120)
        y1 = random.randint(0, 40)
        x2 = random.randint(0, 120)
        y2 = random.randint(0, 40)

        draw.line((x1, y1, x2, y2), fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    font = ImageFont.truetype("/usr/share/fonts/wqy-microhei/wqy-microhei.ttc",20)  #20表示20像素

    str_list = []  #吧每次生成的验证码保存起来
    # 随机生成五个字符
    for i in range(5):
        random_num = str(random.randint(0, 9))  # 随机数字
        random_lower = chr(random.randint(65, 90))  # 随机小写字母
        random_upper = chr(random.randint(97, 122))  # 随机大写字母
        random_char = random.choice([random_num, random_lower, random_upper])
        # print(random_char,"random_char")
        str_list.append(random_char)
        # (5 + i * 24, 10)表示坐标，字体的位置
        draw.text((5+i*24,10),random_char,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),font=font)
    # print(str_list,"str_list")
    f = BytesIO()#内存文件句柄
    img.save(f,"png")   #img是一个对象
    data = f.getvalue()  #读取数据并返回至HTML
    valid_str = "".join(str_list)
    # print(valid_str,"valid_str")
    request.session["keep_valid_code"] = valid_str   #吧保存到列表的东西存放至session中
    return HttpResponse(data)