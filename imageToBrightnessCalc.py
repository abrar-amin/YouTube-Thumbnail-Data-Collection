from PIL import Image, ImageOps
import os
from datetime import date

def measureAverageBrightness(imageName):
    og_image = Image.open(imageName)

    gray_image = ImageOps.grayscale(og_image)
    #gray_image.show()

    pixels = gray_image.load()
    width, height = gray_image.size

    averageColor = 0

    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            averageColor+=cpixel

    averageColor /= (width*height)

    return averageColor


   


