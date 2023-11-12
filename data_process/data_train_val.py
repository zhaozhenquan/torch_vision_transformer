import os
import shutil
import random

# 设置train和val文件夹路径
train_folder = "D:/zzq/learning/torch_vision_transformer/dataset/train"
val_folder = "D:/zzq/learning/torch_vision_transformer/dataset/val"

# 获取train文件夹下所有子文件夹的名称
subfolders = [f for f in os.listdir(train_folder) if os.path.isdir(os.path.join(train_folder, f))]

# 在val文件夹下创建与train相对应的子文件夹
for subfolder in subfolders:
    val_subfolder_path = os.path.join(val_folder, subfolder)
    # os.makedirs(val_subfolder_path, exist_ok=True)

    # 获取train子文件夹下所有图片文件的路径
    train_subfolder_path = os.path.join(train_folder, subfolder)
    image_files = [f for f in os.listdir(train_subfolder_path) if f.endswith(('bmp', '.jpg', '.jpeg', '.png'))]

    # 计算需要移动到val的图片数量
    num_images_to_move = len(image_files) // 5

    # 随机选择要移动的图片
    images_to_move = random.sample(image_files, num_images_to_move)

    # 移动图片到val文件夹对应的子文件夹下
    for image in images_to_move:
        src_path = os.path.join(train_subfolder_path, image)
        dest_path = os.path.join(val_subfolder_path, image)
        shutil.move(src_path, dest_path)

print("图片移动完成。")
