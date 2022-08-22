from tkinter.font import names
from unicodedata import name
from venv import create
from insert import insert
import json
import os
import hashlib
from datetime import datetime
from PIL import Image

ignore_folder = ['.git', '01 app', '01thumbs', "2048", "1920", "800"]
size2048 = (2048, 2048)
size1920 = (1920, 1920)


def resize(imgPath: str, imgName: str, imgSize, imgFolder):

    path = "../{}/{}.png".format(imgFolder, imgName)
    with Image.open(imgPath) as im:
        im.thumbnail(imgSize)
        im.save(path, "PNG")
    return path.replace("..", "")


def handleFolderName(name: str):
    return name.replace("../", "").split("/")[0]


def main(size, folder):
    for dirInfo in os.walk('../source'):
        fdName = handleFolderName(dirInfo[0])
        if fdName not in ignore_folder and fdName != '':
            for img in dirInfo[2]:
                content = "/{}/{}".format(dirInfo[0].replace("../", ""), img)
                imgName = hashlib.md5(content.encode('utf-8')).hexdigest()
                imgPath = "{}/{}".format(dirInfo[0], img)
                print(resize(imgPath, imgName, size, folder))


main(size1920, '1920')
