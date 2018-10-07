# -*- coding: utf-8 -*-
import sys
import numpy as np
from PIL import Image

def binary_dump(text, length):
    binary_text = "".join("{:08b}".format(ord(t)) for t in text)
    dumped = "\n".join(binary_text[i:i+length] for i in range(0,len(binary_text),length))
    print(dumped)
    print(f"{len(binary_text)} bits")
    return binary_text

def hex_dump(text, n):
    hex_nums = ["{:02x}".format(ord(t)) for t in text]
    dumped = "\n".join(" ".join(hex_nums[i:i+n]) for i in range(0, len(hex_nums), n))
    print(dumped)
    print(f"{len(hex_nums) * 4} bits")
    return hex_nums

def picture_dump(text, width, output_filename="out.png"):
    if width % 8 != 0:
        print("Image width should be divisible to 8")
        sys.exit(1)

    binary_text = "".join("{:08b}".format(ord(t)) for t in text)
    if len(binary_text) % width != 0:
        pad_length = width - (width % len(binary_text))
        binary_text = "0"*pad_length + binary_text

    height = len(binary_text) // width
    img_data = []
    for i in range(0,len(binary_text),width):
        data = []
        for j in range(width):
            data += [0] if binary_text[i+j] == "1" else [255]
        img_data += [data]
    print(img_data)
    img = Image.fromarray(np.asarray(dtype=np.dtype('uint8'),a=img_data), mode='L').convert('1')
    img.save(output_filename)
    print(f"{len(binary_text)} bits")

if __name__ == "__main__":
    text = "ABRACADABRA!"
    picture_dump(text,16)


