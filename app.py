# Author: Ali Azhari
# File: app.python
# Date: 08/23/2022

from rembg import remove
from PIL import Image

# make sure you have the picture "old_pic.jpg" in your folder

def remove_bg(input_path):
    try:
        output_path = 'new_' + input_path + '.png'
        inp = Image.open(input_path)
        output = remove(inp)
        output.save(output_path)
    except Exception:
        print('Something went wrong. Goodbye!!')


if __name__ == "__main__":
    input_path =  input("Enter the pics name's: ")
    remove_bg(input_path)
