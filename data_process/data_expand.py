import os
from PIL import Image


def process_folder(folder_path):
    # 获取文件夹下的所有图片文件
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.bmp', 'jpg', '.jpeg', '.png'))]
    # 如果图片数量为1，删除文件夹
    if len(image_files) == 1:
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            os.remove(image_path)
        print(f"Deleting folder: {folder_path}")
        os.rmdir(folder_path)
    elif 1 < len(image_files) < 100:
        # 图片数量大于1且小于100，进行旋转处理
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            img = Image.open(image_path)

            # 旋转图片180度
            rotated_img = img.rotate(180)

            # 保存旋转后的图片
            rotated_file_name = f"{os.path.splitext(image_file)[0]}-rotate180{os.path.splitext(image_file)[1]}"
            rotated_img.save(os.path.join(folder_path, rotated_file_name))

            print(f"Rotated and saved: {rotated_file_name}")


# 设置train文件夹路径
train_folder = "D:/zzq/learning/torch_vision_transformer/dataset/train"

# 遍历train文件夹下所有子文件夹
for subfolder in os.listdir(train_folder):
    subfolder_path = os.path.join(train_folder, subfolder)
    if os.path.isdir(subfolder_path):
        print(subfolder_path)
        process_folder(subfolder_path)

print("处理完成。")
