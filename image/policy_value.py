from PIL import Image, ImageDraw, ImageFont
import numpy as np
from typing import NamedTuple, List, Tuple
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

art=[
    "#############",
    "#           #",
    "#   a       #",
    "#           #",
    "#           #",
    "#     b     #",
    "#           #",
    "#      c    #",
    "#  b        #",
    "#     a     #",
    "#           #",
    "#           #",
    "#############", ]

## 调色板
blue = (0, 64, 254)
red = (254, 0, 64)
yellow = (254, 190, 0)
bg_color = (50, 50, 80)
pall = sns.color_palette(palette="viridis", n_colors=13*13)


def draw(art, bg_color, grid_size=100, gap_size=4, draw_text=True):
    bg_hight = art.shape[1] * (grid_size + gap_size) + gap_size
    bg_weight = art.shape[0] * (grid_size + gap_size) + gap_size
    bg_size = (bg_hight, bg_weight)
    bg_color = (50, 50, 80)

    im = Image.new('RGB', bg_size, bg_color)

    for i in range(art.shape[0]):
        for j in range(art.shape[1]):
            
            color = pall[i*art.shape[1] + j]
            color = tuple([int(x*255) for x in color])
            
            grid_im = Image.new('RGB', (grid_size, grid_size), color)

            paste_pos = (j * (grid_size + gap_size) + gap_size, i * (grid_size + gap_size) + gap_size)
            im.paste(grid_im, paste_pos)

    return im

def modify_corner(im, radius):
    W, H = im.size
    for i in range(radius):
        for j in range(radius):
            x = i
            y = j
            vector = np.array([x - radius+1, y - radius+1], dtype=float)
            if ( np.linalg.norm(vector) > float(radius)):
                im.putpixel((x, y), (255, 255, 255))
                im.putpixel((W-1-x, y), (255, 255, 255))
                im.putpixel((x, H-1-y), (255, 255, 255))
                im.putpixel((W-1-x, H-1-y), (255, 255, 255))

    return im


def draw_polygon():
    pass


if __name__ == '__main__':

    # art = np.array([list(x) for x in art])
    
    grid_size, gap_size = 100, 4

    # im = draw(art, bg_color, grid_size=grid_size, gap_size=gap_size, draw_text=False)
    # im = im.convert('RGBA')

    # im.show()
    # im.save('policy_value.bmp')
    
    im = Image.new('RGB', (1000, 500), bg_color)
    im = im.convert('RGBA')

    # Draw red and yellow triangles on it and save
    draw = ImageDraw.Draw(im)
    draw.polygon([(0, 200), (0, 300), (300,250)], fill = (255,255,255, 0))

    im.show()