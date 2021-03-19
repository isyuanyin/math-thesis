from PIL import Image, ImageDraw, ImageFont
import numpy as np
from typing import NamedTuple, List, Tuple


class GridworldObject(NamedTuple):
    n: int
    reward: float
    eps_term: float
    eps_respawn: float
    symbol: chr

class GridworldConfig(NamedTuple):
    art: List[str]
    objects: Tuple[GridworldObject]
    max_steps: int
    discount: float = 0.99

DENSE = GridworldConfig(
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
        "#############",
    ],
    objects=tuple(
        map(
            lambda x: GridworldObject(*x),
            [
                (2, 1.0, 0.0, 0.05, "a"),
                (1, -1.0, 0.5, 0.1, "b"),
                (1, -1.0, 0.0, 0.5, "c"),
            ],
        )
    ),
    max_steps=500,
)

SPARSE = GridworldConfig(
    art=[
        "###############",
        "#             #",
        "#             #",
        "#             #",
        "#             #",
        "#             #",
        "#             #",
        "#             #",
        "#             #",
        "#             #",
        "#             #",
        "#             #",
        "#             #",
        "#             #",
        "###############",
    ],
    objects=tuple(
        map(
            lambda x: GridworldObject(*x),
            [(1, 1.0, 1.0, 0.0, "a"), (1, -1.0, 1.0, 0.0, "b")],
        )
    ),
    max_steps=50,
)

LONG_HORIZON = GridworldConfig(
    art=[
        "#############",
        "#           #",
        "#           #",
        "#           #",
        "#           #",
        "#           #",
        "#           #",
        "#           #",
        "#           #",
        "#           #",
        "#           #",
        "#           #",
        "#############",
    ],
    objects=tuple(
        map(
            lambda x: GridworldObject(*x),
            [(2, 1.0, 0.0, 0.01, "a"), (2, -1.0, 0.5, 1.0, "b")],
        )
    ),
    max_steps=1000,
)

LONGER_HORIZON = GridworldConfig(
    art=[
        "###########",
        "#    #    #",
        "#         #",
        "#    #    #",
        "#   ###   #",
        "#    #    #",
        "#         #",
        "#    #    #",
        "###########",
    ],
    objects=tuple(
        map(
            lambda x: GridworldObject(*x),
            [
                (2, 1.0, 0.1, 0.01, "a"),
                (5, -1.0, 0.8, 1.0, "b"),
            ],
        )
    ),
    max_steps=2000,
)

LONG_DENSE = GridworldConfig(
    art=[
        "#############",
        "#           #",
        "#     #     #",
        "#     #     #",
        "#     #     #",
        "### ##### ###",
        "#     #     #",
        "#     #     #",
        "#           #",
        "#     #     #",
        "#     #     #",
        "#     #     #",
        "### ##### ###",
    ],
    objects=tuple(
        map(
            lambda x: GridworldObject(*x),
            [
                (4, 1.0, 0.0, 0.005, "a"),
            ],
        )
    ),
    max_steps=2000,
)

SMALL = GridworldConfig(
    art=[
        "#########",
        "#       #",
        "#  #    #",
        "#       #",
        "#    #  #",
        "#       #",
        "#########",
    ],
    objects=tuple(
        map(
            lambda x: GridworldObject(*x),
            [
                (2, 1.0, 0.0, 0.05, "a"),
                (2, -1.0, 0.5, 0.1, "b"),
            ],
        )
    ),
    max_steps=500,
)

SMALL_SPARSE = GridworldConfig(
    art=[
        "#########",
        "#       #",
        "#       #",
        "#       #",
        "#       #",
        "#       #",
        "#########",
    ],
    objects=tuple(
        map(
            lambda x: GridworldObject(*x),
            [
                (1, 1.0, 1.0, 1.0, "a"),
                (2, -1.0, 1.0, 1.0, "b"),
            ],
        )
    ),
    max_steps=50,
)

VERY_DENSE = GridworldConfig(
    art=[
        "#############"
        "#           #"
        "#           #"
        "#           #"
        "#           #"
        "#           #"
        "#           #"
        "#           #"
        "#           #"
        "#           #"
        "#           #"
        "#           #"
        "#############"
    ],
    objects=tuple(
        map(
            lambda x: GridworldObject(*x),
            [
                (1, 1.0, 0.0, 1.0, "a"),
            ],
        )
    ),
    max_steps=2000,
)

blue = (0, 64, 254)
red = (254, 0, 64)
yellow = (254, 190, 0)

def draw(art, bg_color, grid_size=100, gap_size=4, draw_text=True):
    bg_hight = art.shape[1] * (grid_size + gap_size) - gap_size
    bg_weight = art.shape[0] * (grid_size + gap_size) - gap_size
    bg_size = (bg_hight, bg_weight)
    im = Image.new('RGB', bg_size, bg_color)

    for i in range(art.shape[0]):
        for j in range(art.shape[1]):
            color_dit = {'#': bg_color, ' ': 'white', 'a': blue, 'b': red, 'c': yellow}
            color = color_dit[art[i][j]]
            
            grid_im = Image.new('RGB', (grid_size, grid_size), color)

            if draw_text:
                draw = ImageDraw.Draw(grid_im)
                
                myfont = ImageFont.truetype('Arial.ttf', size=80)
                if art[i][j] == 'a':
                    draw.text(xy=(0, 0), text="1.0", font=myfont, fill='black')
                    grid_im.show()

            paste_pos = (j * (grid_size + gap_size), i * (grid_size + gap_size))
            im.paste(grid_im, paste_pos)

    return im


class GridMaps(NamedTuple):
    DENSE = DENSE
    SPARSE = SPARSE
    LONG_HORIZON = LONG_HORIZON
    LONGER_HORIZON = LONGER_HORIZON
    LONG_DENSE = LONG_DENSE
    SMALL = SMALL
    SMALL_SPARSE = SMALL_SPARSE
    VERY_DENSE = VERY_DENSE


if __name__ == '__main__':
    bg_color = (50, 50, 80)
    game_config = GridMaps.DENSE
    art = np.array([list(x) for x in game_config.art])
    
    im = draw(art, bg_color, grid_size=100, gap_size=4, draw_text=False)
    im.show()
    im.save('long_dense.svg')