import torch
import cv2
import pyttsx3
import threading
from queue import Queue

# 加载模型
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\Fergus\\Desktop\\yolov5\\runs\\train\\exp9\\weights\\best.pt')

# 定义类别名称
class_names = ['grapejuice', 'hokkaido']  # 替换为你的类别名称

# 获取摄像头输入
cap = cv2.VideoCapture(0)  # 0 表示第一个摄像头

# 初始化语音合成器
engine = pyttsx3.init()

# 语音播报队列
speech_queue = Queue()

# 函数：语音播报物体种类
def speak_objects():
    while True:
        class_name = speech_queue.get()
        engine.setProperty('rate', 150) 
        engine.say('this is ' + class_name)
        engine.runAndWait()
        speech_queue.task_done()

# 函数：处理识别结果并绘制到图像
def process_results(frame, results):
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
            
            # 将物体种类加入语音播报队列
            speech_queue.put(class_name)

# 函数：视频流处理
def video_stream():
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 使用模型进行推理
        results = model(frame)

        # 处理识别结果并绘制到图像
        process_results(frame, results)

        # 显示结果
        cv2.imshow('Real-time Object Detection', frame)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 启动语音播报线程
speech_thread = threading.Thread(target=speak_objects)
speech_thread.daemon = True
speech_thread.start()

# 启动视频流处理线程
video_thread = threading.Thread(target=video_stream)
video_thread.start()

# 等待线程结束
video_thread.join()

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()
