from PIL import Image
import os

filename = "marvin.gif"
im = Image.open(filename)
if im.mode == "RGBA":
   im = im.convert("RGB")
new_filename = "sql1.pdf"
if not os.path.exists(new_filename):
    im.save(new_filename, "PDF", resolution = 1000.0)
