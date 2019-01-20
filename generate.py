#!/usr/bin/env python3

from subprocess import call
from sys import argv
from sys import exit


font_file = "./assets/font.otf"
backdrop_file = "./assets/backdrop.gif"
font_size = "120"
font_color = "#40C4FB"

version = argv[1]


call([
    "magick",
    backdrop_file,
    "-pointsize",
    font_size,
    "-fill",
    font_color,
    "-font",
    font_file,
    "-draw",
    "gravity Center text 0,0 " + version,
    "./build/" + version + ".gif",
])
