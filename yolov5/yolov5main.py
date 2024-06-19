import torch
from PIL import Image
import cv2

model = torch.hub.load('ultralytics/yolov5:v6.0', 'custom', path=r'C:\Users\Fergus\Desktop\yolov5\runs\train\exp\weights\best.pt', force_reload=True)


cap = cv2.VideoCapture(0)

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
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    annotated_frame = results.render()[0]

    # 在窗口中显示图像
    cv2.imshow("Object Detection", annotated_frame)

    # 退出键：'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#python train.py --img-size 640 --batch-size 16 --epochs 50 --data "C:\Users\Fergus\Desktop\yolov5\data.yaml" --cfg models/yolov5s.yaml --weights yolov5s.pt
