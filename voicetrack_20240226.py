'''
Date: 2024-02-26 13:48:51
LastEditors: Fuwaa kongzt@yeah.net
LastEditTime: 2024-05-31 16:39:04
FilePath: \yolov5\voicetrack_20240226.py
'''
# -*- coding: utf-8 -*-

import torch
import cv2
import pyttsx3

# 加载模型
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\Fergus\\Desktop\\yolov5\\runs\\train\\exp40\\weights\\best.pt')

# 定义类别名称
class_names = ['Meiji','Morinaga','Hokkaido','Grapejuice', 'Yotsubateshibo']  # 替换为你的类别名称

# 获取摄像头输入
cap = cv2.VideoCapture(1)  # 0 表示第一个摄像头

# 初始化语音合成器
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    if 'Japanese' in voice.languages:
        engine.setProperty('voice', voice.id)
        break

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 使用模型进行推理
    results = model(frame)

    # 获取预测结果
    pred = results.pred[0]
    pred_boxes = pred[:, :4].cpu().numpy().astype(int)
    pred_confidences = pred[:, 4].cpu().numpy()
    pred_classes = pred[:, 5].cpu().numpy().astype(int)

    # 在图像上绘制识别结果
    for box, conf, class_id in zip(pred_boxes, pred_confidences, pred_classes):
        if conf > 0.7:  # 可以调整置信度阈值
            class_name = class_names[class_id]
            x1, y1, x2, y2 = box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{class_name}: {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            engine.setProperty('rate', 300) 
            
            # 语音播报物体种类
            engine.say('これは'+class_name)
            engine.runAndWait()

    # 显示结果
    cv2.imshow('Real-time Object Detection', frame)

    # 按下 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()

