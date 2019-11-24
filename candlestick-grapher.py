import sys
import pygame
import numpy as np
from PIL import Image
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '0, 30'
pygame.init()
size = width, height = 2560, 1050
screen = pygame.display.set_mode(size)
img = Image.new('RGB', (width, height), 'white')
pixels = img.load()
stockdatafile = input('stock data filepath: ')      
imagesavelocation = input('image save filepath: ')  
f = open(stockdatafile, 'r')
linecounter = 0
atl = 0
ath = 0
for line in f.readlines():
    if linecounter == 0:
        atl = float(line.split(',')[4])
    atl = min(atl, float(line.split(',')[4]))
    ath = max(ath, float(line.split(',')[3]))
    linecounter += 1
print(ath, atl, (height - 2) / (ath - atl))
totallines = linecounter
f.close()
linecounter = 0
candlecounter = 0
flis = True
f = open(stockdatafile, 'r')
rg = (0, 0, 0)
oppoint, hipoint, lopoint = [0, ]*3
for line in f.readlines():
    if flis:
        oppoint, hipoint, lopoint = [int(round((height - 2) / (ath - atl) * float(i))) for i in line.split(',')[2:5]]
        flis = False
    hipoint = max(hipoint, int(round((height - 2) / (ath - atl) * float(line.split(',')[3]))))
    lopoint = min(lopoint, int(round((height - 2) / (ath - atl) * float(line.split(',')[4]))))
    if candlecounter < (width - 1) // 4 and linecounter % (totallines // ((width - 1) // 4)) == 0 < linecounter:
        clpoint = int(round((height - 2) / (ath - atl) * float(line.split(',')[5])))
        rg = (0, 255, 0) if clpoint > oppoint else (255, 0, 0) if oppoint > clpoint else (0, 0, 0)
        for i in range(hipoint - lopoint + 1):
            rg = (0, 0, 0) if (hipoint - i >= max(oppoint, clpoint) or hipoint - i <= min(oppoint, clpoint)) \
                else (0, 255, 0) if clpoint > oppoint else (255, 0, 0) if oppoint > clpoint else (0, 0, 0)
            pixels[2 + candlecounter * 4, (height - 2) / (ath - atl) * atl +
                   ((height - 1) - hipoint + i)] = rg
        for i in range(abs(clpoint - oppoint) + 1):
            pixels[2 + candlecounter * 4 - 1, (height - 2) / (ath - atl) * atl +
                   ((height - 1) - max(oppoint, clpoint) + i)] = (0,)*3
            pixels[2 + candlecounter * 4 + 1, (height - 2) / (ath - atl) * atl +
                   ((height - 1) - max(oppoint, clpoint) + i)] = (0,)*3
        candlecounter += 1
        flis = True
    linecounter += 1

img.save(imagesavelocation, compress_level=0)

pgimg = pygame.image.load(imagesavelocation)
ballrect = pgimg.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # screen.fill(black)
    screen.blit(pgimg, ballrect)
    pygame.display.flip()
