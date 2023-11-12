import os
import fnmatch

# 设置train文件夹路径
train_folder = "D:/zzq/learning/torch_vision_transformer/dataset/train"

# 遍历train文件夹下所有子文件夹
for subfolder in os.listdir(train_folder):
    subfolder_path = os.path.join(train_folder, subfolder)

    # 检查是否是文件夹
    if os.path.isdir(subfolder_path):
        # 获取子文件夹下的所有图片文件
        image_files = [f for f in os.listdir(subfolder_path) if f.endswith(('bmp','.jpg', '.jpeg', '.png'))]

        # 检查图片名称是否包含rotate180，如果是，则删除该图片
        for image_file in image_files:
            if "rotate180" in image_file:
                image_path = os.path.join(subfolder_path, image_file)
                os.remove(image_path)
                print(f"Deleted: {image_path}")

print("处理完成。")
