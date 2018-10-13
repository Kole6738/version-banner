#!/usr/bin/env python3

from subprocess import call
from sys import argv
from sys import exit
from sys import platform


backdrop_file = "./assets/backdrop.gif"
font_size = "120"
font_color = "#40C4FB"

if platform == "linux":
    font_file_path = "/usr/share/fonts/"
if platform == "darwin":
    font_file_path = "/Library/Fonts/"
elif platform == "win32":
    font_file_path = "C:/Windows/Fonts/"

if not font_file_path:
    exit(1)

font_file_name = font_file_path + "UNI SANS HEAVY.OTF"

version = argv[1]


call([
    "magick",
    backdrop_file,
    "-pointsize",
    font_size,
    "-fill",
    font_color,
    "-font",
    font_file_name,
    "-draw",
    "gravity Center text 0,0 " + version,
    "./build/" + version + ".gif",
])
