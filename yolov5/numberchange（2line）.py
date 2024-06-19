'''
Date: 2024-06-02 03:40:51
LastEditors: Fuwaa kongzt@yeah.net
LastEditTime: 2024-06-02 03:43:58
FilePath: \yolov5\numberchange（2line）.py
'''
import os

def modify_files(directory):
    # 遍历指定目录下的所有txt文件
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()

            # 确保文件至少有两行
            if len(lines) >= 2:
                # 修改第一行的第一个数字
                lines[0] = '3' + lines[0][1:]
                # 修改第二行的第一个数字
                lines[1] = '6' + lines[1][1:]

            # 写入修改后的内容
            with open(filepath, 'w') as file:
                file.writelines(lines)

# 调用函数，你需要替换'DIRECTORY_PATH'为你的txt文件所在的文件夹路径
modify_files(r'C:\Users\Fergus\Desktop\img\useddata\yuki\obj_train_data')
