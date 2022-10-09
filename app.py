from rembg import remove
from PIL import Image

# make sure you have the picture "old_pic.jpg" in your folder
input_path = 'old_pic.jpg'
output_path = 'new_pic.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)