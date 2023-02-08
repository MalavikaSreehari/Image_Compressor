import PIL
from PIL import Image
from tkinter.filedialog import *

file_path= askopenfilename()
Image = PIL.Image.open(file_path)
height,width = Image.size
Img=Image.resize((height,width), PIL.Image.LANCZOS)
save_path = asksaveasfilename()
Img=Img.convert("RGB")
Img.save(save_path+"_resized.jpeg")