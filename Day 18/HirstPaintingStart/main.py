###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
from pathlib import Path
import colorgram

image_path = Path(__file__).resolve().parent / "image.jpg"

rgb_colors = []
colors = colorgram.extract(str(image_path), 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)