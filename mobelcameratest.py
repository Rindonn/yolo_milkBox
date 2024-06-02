# coding=utf-8
import cv2
import time
import os
 
if os.path.exists('img') == False:
    os.mkdir('img')
filenames = os.listdir(r'img')
 
if __name__ == '__main__':
 
    # 开启ip摄像头
    cv2.namedWindow("camera", 1)
    # 这个地址就是下面记下来的局域网IP
    video = "http://admin:admin@172.18.34.121:8081/"  # 此处@后的ipv4 地址需要修改为自己的地址
    
    capture = cv2.VideoCapture(video)
 
    num = len(filenames)
    index = 0
    imgname = -1
    while True:
        success, img = capture.read()
 
        # 不进行旋转
        cv2.imshow("camera", img)
 
        # 获取长宽
        # (h, w) = img.shape[:2]
        # center = (w // 2, h // 2)
        # 进行旋转
        # M = cv2.getRotationMatrix2D(center, -90, 1.0)
        # rotated = cv2.warpAffine(img, M, (w, h))
        # 若不关参数，参数也会被旋转，影响效果
        # cv2.imshow("camera", rotated)
 
        # 按键处理，注意，焦点应当在摄像头窗口，不是在终端命令行窗口
        key = cv2.waitKey(10)
 
        if key == 27:
            # 按esc键退出
            print("esc break...")
            break
 
        if key == ord(' '):
            # 按空格 保存图像 图片的路径
            while True:
                index = index + 1
                success, img = capture.read()
                cv2.imshow("camera", img)
                cv2.waitKey(10)
                if index == 15:
                    num = num + 1
                    imgname = imgname + 1
                    if imgname == -1:  # 此处改为-1为无限截取图片
                        break
                    filename = "img\\frames_%s.jpg" % (num)
                    cv2.imwrite(filename, img)
                    index = 0
 
    capture.release()
    cv2.destroyWindow("camera")
 