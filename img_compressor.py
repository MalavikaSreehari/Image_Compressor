import PIL
from PIL import Image
from tkinter.filedialog import *

file_path= askopenfilename()
Image = PIL.Image.open(file_path)
height,width = Image.size
Img=Image.resize((height,width), PIL.Image.LANCZOS)
save_path = asksaveasfilename()
Img=Img.convert("RGB")
# im = Image.open(Img)
# rgb_im = im.convert('RGB')
# rgb_im.save(save_path+"_resized.jpeg")
Img.save(save_path+"_resized.jpeg")