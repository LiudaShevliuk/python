#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
from random  import randint
from re import findall

def encrypt():
    image = Image.open(input('Enter path to image: '))
    text = input('Enter your message: ')
    draw = ImageDraw.Draw(image)
    width, height = image.size
    pixels = image.load()
    f = open('positions.txt', 'w')

    for i in ([ord(i) for i in text]):
        key = (randint(1, width-10), randint(1, height-10))
        g, b = pixels[key][1:3]
        draw.point(key, (i,g,b))
        f.write(str(key) + '\n')

    image.save('newimage.png', 'png')
    f.close()

def decrypt():
    text = []						    
    keys = []
    new_image = Image.open('./newimage.png')
    new_image.show()				
    pixels = new_image.load()
    f = open('positions.txt', 'r')
    keys_str = str([line.strip() for line in f])				
															
    for i in range(len(findall(r'\((\d+)\,', keys_str))):
        keys.append((int(findall(r'\((\d+)\,', keys_str)[i]), \
                    int(findall(r'\,\s(\d+)\)', keys_str)[i]))) 

    f.close()
	
    for key in keys:
        text.append(pixels[tuple(key)][0])	
						
    return ''.join([chr(elem) for elem in text])	

encrypt()
print("Your message is: ", decrypt())
