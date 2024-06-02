import torch
from pathlib import Path
from PIL import Image
import cv2
import numpy as np
import torch



# 载入训练好的模型，替换为你的模型路径
model = torch.hub.load('ultralytics/yolov5:v7.0', 'custom', path=r'C:\Users\Fergus\Desktop\yolov5\runs\train\exp\weights\best.pt', force_reload=True)

# 读取视频文件
video_path = r'C:\Users\Fergus\Desktop\img\grapetest.mp4'  # 替换为你的视频文件路径
cap = cv2.VideoCapture(video_path)

# 视频输出设置
output_path = r'C:\Users\Fergus\Desktop\yolov5'  # 替换为你的输出视频文件路径
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # 将 OpenCV BGR 图像转换为 RGB PIL 图像
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # 进行物体识别
    results = model(img)

    # 在图像上绘制边界框
    annotated_frame = np.array(results.render()[0])

    # 在窗口中显示图像
    cv2.imshow("Object Detection", annotated_frame)

    # 写入视频文件
    out.write(annotated_frame)

    # 退出键：'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
