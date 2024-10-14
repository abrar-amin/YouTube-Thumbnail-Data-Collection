from PIL import Image, ImageOps
import os
from datetime import date

def measureAverageBrightness(imageName):
    og_image = Image.open(imageName)

    hsv_image = og_image.convert('HSV')
    #gray_image.show()

    pixels = hsv_image.load()
    width, height = hsv_image.size

    averageSaturation = 0

    for x in range(width):
        for y in range(height):
                hsv = hsv_image.getpixel((x,y))
                averageSaturation += hsv[1]


    averageSaturation /= (width*height)

    return averageSaturation




   


