import sys
import os

def rename(path):
	index = 0
	for image in os.listdir(path):
		index += 1
		image = image.strip()
		name = image.split('.')[0]
		suffix = image[len(name) + 1: len(image)]
		str_name = '%d' %index
		os.rename(os.path.join(path, image), os.path.join(path, str_name + '.' + suffix)) 
	print('OK')

path = '/home/sci/src/BOW/dataset/train/'
rename(path)