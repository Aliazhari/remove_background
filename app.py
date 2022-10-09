from rembg import remove
from PIL import Image

input_path = 'ali1.png'
output_path = 'ali.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)