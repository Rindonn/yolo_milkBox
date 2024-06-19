import torch
import cv2
from PIL import Image
import time  # 导入时间模块

# 指定 YOLOv5 模型的本地路径
model_path = 'C:\\Users\\Fergus\\Desktop\\yolov5\\runs\\train\\exp6\\weights\\best.pt'

# 加载 YOLOv5 模型
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

# 获取模型对象
if isinstance(model, tuple):
    model = model[0]

# 打开摄像头
cap = cv2.VideoCapture(0)  # 参数 0 表示打开默认摄像头

while cap.isOpened():
    # 读取摄像头图像
    ret, frame = cap.read()
    if not ret:
        break

    # 将 OpenCV 图像格式转换为 PIL 图像格式
    image = Image.fromarray(frame[..., ::-1])

    # 进行物体检测
    with torch.no_grad():
        results = model(image)

    # 获取检测结果的图像
    output_image = results.render()[0]

    # 将 PIL 图像转换为 OpenCV 图像格式
    output_frame = cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR)

    # 显示检测结果
    cv2.imshow('Object Detection', output_frame)

    # 等待一段时间（例如30毫秒），如果用户按下 'q' 键则退出
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()