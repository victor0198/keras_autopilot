from PIL import Image
import os

directs = ['_1/','_2/','_3/','0/','1/','2/','3/']
size = 200, 66
for direct in directs:
	for img in os.listdir(direct):
		im = Image.open(direct+img)
		im_resized = im.resize(size, Image.ANTIALIAS)
		im_resized.save(direct+img)
