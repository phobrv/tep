from tkinter.font import names
from unicodedata import name
from venv import create
from insert import insert
import json
import os
import hashlib
from datetime import datetime
from PIL import Image

ignore_folder = ['.git', '01app', '01thumbs']
git_link = "https://raw.githubusercontent.com/phobrv/tep/main"
print(hashlib.md5("whatever your string is".encode('utf-8')).hexdigest())


def handleFolderName(name: str):
    return name.replace("../", "").split("/")[0]


def handleCreatedAt(createStr: str):
    nameSplit = createStr.split(",")
    if len(nameSplit) == 1:
        createStr = datetime.strptime(createStr, "%d %B %Y")
    elif(len(nameSplit) > 2):
        createStr = "{}, {}".format(nameSplit[-2].strip(), nameSplit[-1].strip())
        createStr = datetime.strptime(createStr, "%B %d, %Y")

    return createStr


def create_thumb(path: str, thumb: str):
    size = (128, 128)
    pathThumb = "../01thumbs/{}.png".format(thumb)
    with Image.open(path) as im:
        im.thumbnail(size)
        im.save(pathThumb, "PNG")
    return pathThumb.replace("..", "")


def insertImg():
    for dirInfo in os.walk('../'):
        fdName = handleFolderName(dirInfo[0])
        if fdName not in ignore_folder and fdName != '':
            created_at = handleCreatedAt(fdName)
            for img in dirInfo[2]:
                content = "/{}/{}".format(dirInfo[0].replace("../", ""), img)
                title = hashlib.md5(content.encode('utf-8')).hexdigest()
                thumb = create_thumb("{}/{}".format(dirInfo[0], img), title)
                payload = json.dumps({
                    "title": title,
                    "slug": title,
                    "thumb": thumb,
                    "content": content,
                    "excerpt": git_link,
                    "created_at": str(created_at)
                })
                insert(payload)


# insertImg()
