from PIL import Image
import os
import random
import string

def digit_generator():

    letters = string.digits
    result_str = ''.join(random.choice(letters) for _ in range(6))
    return result_str

def convert(path,name):

    file_name = name+".png"
    img = Image.open(path)
    img.save(file_name,bitmap_format='png')

def make_folder(name):

    f_name = name+".png"
    os.makedirs('jpg to png',exist_ok = True)
    os.rename(f_name,'jpg to png/'+f_name)

digit = digit_generator()

path = input("Enter file fullname(with .jpg) :")

file_name = convert(path,digit)
make_folder(digit)
print("done!bye")