'''
Date: 2024-05-29 14:45:11
LastEditors: Fuwaa kongzt@yeah.net
LastEditTime: 2024-06-02 03:46:23
FilePath: \yolov5\number_change.py
'''
import os

# 设置您文本文件所在的目录
directory = r'C:\Users\Fergus\Desktop\img\useddata\FantaOrange\obj_train_data'

# 指定从第几个文件开始修改
start_index = 0  # 从第10个文本文件开始修改

# 指定要修改的文件数量
number_of_files_to_modify = 10000  # 修改接下来的50个文件

# 初始化一个计数器
count = 0

# 获取目录中所有文本文件的列表
all_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

# 确保文件列表足够长
if start_index + number_of_files_to_modify > len(all_files):
    number_of_files_to_modify = len(all_files) - start_index

# 遍历指定范围内的文件
for filename in all_files[start_index:start_index + number_of_files_to_modify]:
    file_path = os.path.join(directory, filename)  # 获取文件的完整路径
    with open(file_path, 'r') as file:
        content = file.read()  # 读取文件内容

    # 检查第一个字符是否为 '0'
    if content.startswith('4'):
        new_content = '8' + content[1:]  # 将第一个字符替换为 '1'
        
        # 将新内容写回文件
        with open(file_path, 'w') as file:
            file.write(new_content)
        
        # 更新计数器
        count += 1

print(f"从第 {start_index+1} 个文件开始，已更新 {count} 个文件。")
