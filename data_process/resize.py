from PIL import Image
import os

# 设置train文件夹路径
train_folder = "D:/zzq/learning/torch_vision_transformer/dataset/val"

# 遍历train文件夹下所有子文件夹
for subfolder in os.listdir(train_folder):
    subfolder_path = os.path.join(train_folder, subfolder)

    # 检查是否是文件夹
    if os.path.isdir(subfolder_path):
        # 获取子文件夹下的所有图片文件
        image_files = [f for f in os.listdir(subfolder_path) if f.endswith(('bmp', '.jpg', '.jpeg', '.png'))]

        # 修改图片尺寸为256*256
        for image_file in image_files:
            image_path = os.path.join(subfolder_path, image_file)
            img = Image.open(image_path)

            # 修改图片尺寸
            img_resized = img.resize((224, 224))

            # 保存修改尺寸后的图片
            img_resized.save(image_path)

            print(f"Resized: {image_path} to 224x224")

print("处理完成。")
