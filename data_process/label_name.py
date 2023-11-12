import os

# 设置train文件夹路径
train_folder = "D:/zzq/learning/torch_vision_transformer/dataset/train"

# 获取train文件夹下所有子文件夹的名称
subfolders = [f for f in os.listdir(train_folder) if os.path.isdir(os.path.join(train_folder, f))]

# 构建字符串，每个子文件夹名称用英文双引号包起来，用英文逗号隔开
result = ",".join([f'"{subfolder}"' for subfolder in subfolders])

print(result)