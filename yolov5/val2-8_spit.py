'''
Date: 2024-05-29 16:06:28
LastEditors: Fuwaa kongzt@yeah.net
LastEditTime: 2024-05-29 16:14:00
FilePath: \yolov5\models\val2-8_spit.py
'''
import os
import shutil
from sklearn.model_selection import train_test_split

# 指定原始图像和标签的目录
images_dir = r'C:\Users\Fergus\Desktop\yolov5\dataset\images\train'
labels_dir = r'C:\Users\Fergus\Desktop\yolov5\dataset\labels\train'

# 指定新的验证集目录
val_images_dir = r'C:\Users\Fergus\Desktop\yolov5\dataset\images\val'
val_labels_dir = r'C:\Users\Fergus\Desktop\yolov5\dataset\labels\val'

# 创建验证集目录，如果不存在的话
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# 获取所有图像文件的完整路径
image_paths = [os.path.join(images_dir, f) for f in os.listdir(images_dir) if f.endswith('.jpg')]
label_paths = [os.path.join(labels_dir, f.replace('.jpg', '.txt')) for f in os.listdir(images_dir) if f.endswith('.jpg')]

# 使用train_test_split分割数据集，这里分割20%为验证集
train_imgs, val_imgs, train_labels, val_labels = train_test_split(image_paths, label_paths, test_size=0.2, random_state=42)

# 移动选中的验证集图像及其标签到新目录
for val_image, val_label in zip(val_imgs, val_labels):
    # 获取文件名
    image_filename = os.path.basename(val_image)
    label_filename = os.path.basename(val_label)
    
    # 目标文件路径
    target_image_path = os.path.join(val_images_dir, image_filename)
    target_label_path = os.path.join(val_labels_dir, label_filename)

    # 移动文件
    shutil.move(val_image, target_image_path)
    shutil.move(val_label, target_label_path)

print(f"已移动 {len(val_imgs)} 对图像和标签到验证集目录。")
