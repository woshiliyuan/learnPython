# encoding=utf-8
"""
如何调用AI api接口
手势识别： https://console.faceplusplus.com.cn/documents/10065649
"""

import base64
import json

import cv2
import numpy
import requests
from PIL import Image, ImageFont


# 感觉这个返回值设计的不够简洁，最后的结果相加为100，取最大值吧
def solve_gesture_response(gesture):
    maxValue = 0
    result = 'unknown'
    for key, value in gesture.items():
        if value > maxValue:
            result = key
    translate_gesture = {"unknown": "未定义手势", "heart_a": "爱心", "heart_d": "比心", "victory": "胜利"}
    print("result", result)
    if result in translate_gesture:
        result = translate_gesture[result]
    return result


# 如果不在图片上绘制中文文本就可以删除本函数
def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=50):
    if (isinstance(img, numpy.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = Image.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype("font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)


def reg_gesture(img_name):
    beautify_url = "https://api-cn.faceplusplus.com/humanbodypp/v1/gesture"

    # 1. 二进制方式打开图片
    f = open(img_name, 'rb')
    # 转 base64
    img_base64 = base64.b64encode(f.read())

    # 使用 whitening、smoothing、thinface 三个可选参数，其他用默认值
    data = {
        'api_key': '0HJ-21HLanuZRIpX4f_BhNL1LmA5RYZ-',
        'api_secret': '7BKF_LRlPa6KH2wO_yVMUUG_fUzkasFS',
        'image_base64': img_base64,
        'return_gesture': 1
    }

    # 2. 调用接口
    r = requests.post(url=beautify_url, data=data)
    html = json.loads(r.text)

    # 3. 解码返回图片
    # response中将整个图片以base64的格式返回，需要解码
    hands = html['hands']
    print("hands: ", hands)

    # 4. 显示图片: 绘制矩形，添加文本
    img = cv2.imread(img_name)
    # 绘制矩形
    colors = (0, 0, 255)
    left = int(hands[0]['hand_rectangle']['left'])
    top = int(hands[0]['hand_rectangle']['top'])
    width = int(hands[0]['hand_rectangle']['width'])
    height = int(hands[0]['hand_rectangle']['height'])
    cv2.rectangle(img, (left, top), (left + width, top + height), colors, 5)

    gesture_result = solve_gesture_response(hands[0]['gesture'])
    # 图片，添加的文字（醉醉的，中文会乱码），左上角坐标(整数)，字体，字体大小，颜色，字体粗细
    # cv2.putText(img, gesture_result, (left+100,top+100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 3)
    img = cv2ImgAddText(img, gesture_result, left + 100, top + 100)

    cv2.imshow('hehe', img)
    cv2.waitKey(0)


reg_gesture("heart2.jpg")
