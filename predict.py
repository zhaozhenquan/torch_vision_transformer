# -*- coding: utf-8 -*-
# @File : predict.py
# @Author: Runist
# @Time : 2021/12/14 16:15
# @Software: PyCharm
# @Brief:


import os

import torch
from PIL import Image

from dataloader import data_transform
from utils import create_model, model_parallel
from config import args


def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # load image
    image_path = "./data_test/val/daisy/54377391_15648e8d18.jpg"
    assert os.path.exists(image_path), "file: '{}' dose not exist.".format(image_path)

    image = Image.open(image_path)

    # [N, C, H, W]
    image = data_transform["val"](image)
    # expand batch dimension
    image = torch.unsqueeze(image, dim=0)

    # create model
    model = create_model(args)
    model = model_parallel(args, model).to(device)
    # load model weights
    model_weight_path = "./summary/vit_base_patch16_224/weights/epoch=22_val_acc=0.9619.pth"
    model.load_state_dict(torch.load(model_weight_path, map_location=device))

    model.eval()
    with torch.no_grad():
        # predict class
        output = torch.squeeze(model(image.to(device))).cpu()
        predict = torch.softmax(output, dim=0)
        index = torch.argmax(predict).numpy()

    print("prediction: {}   prob: {:.3}\n".format(args.label_name[index],
                                                predict[index].numpy()))
    for i in range(len(predict)):
        print("class: {}   prob: {:.3}".format(args.label_name[i],
                                               predict[i].numpy()))


if __name__ == '__main__':
    main()
