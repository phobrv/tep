from tkinter.font import names
from unicodedata import name
from venv import create
from insert import insert
import json
import os
import hashlib
from datetime import datetime
from PIL import Image
from os.path import exists


ignore_img = ['.DS_Store']
git_link = "https://raw.githubusercontent.com/phobrv/tep/main"

size1920 = (1920, 1920)
size800 = (800, 800)
sizeThumb = (256, 256)
fmts = ("%d %B %Y", "%B %d, %Y")


def handleFolderName(name: str):
    return name.replace("../source/", "")


def handleDateFormat(dateStr: str):
    for fmt in fmts:
        try:
            return datetime.strptime(dateStr, fmt)
        except Exception as e:
            pass


def handleCreatedAt(createStr: str):
    dateOut = handleDateFormat(createStr)
    if dateOut is None:
        nameSplit = createStr.split(",")
        if(len(nameSplit) > 2):
            createStr = "{}, {}".format(nameSplit[-2].strip(), nameSplit[-1].strip())
            dateOut = handleDateFormat(createStr)
        if dateOut is None:
            createStr = nameSplit[-1].strip()
            dateOut = handleDateFormat(createStr)
    return dateOut


def resize(imgPath: str, imgName: str, imgSize, imgFolder):
    path = "../{}/{}.png".format(imgFolder, imgName)
    if exists(path) == False:
        with Image.open(imgPath) as im:
            im.thumbnail(imgSize)
            im.save(path, "PNG")
        return path.replace("..", "")
    else:
        print(imgName, imgFolder, "exist")


def insertImg():
    for dirInfo in os.walk('../source'):
        fdName = handleFolderName(dirInfo[0])
        if fdName != '':
            created_at = handleCreatedAt(fdName)
            if created_at is not None:
                for img in dirInfo[2]:
                    if img not in ignore_img:
                        content = "/{}/{}".format(dirInfo[0].replace("../", ""), img)
                        imgName = hashlib.md5(content.encode('utf-8')).hexdigest()
                        imgPath = "{}/{}".format(dirInfo[0], img)
                        thumb = imgName+".png"
                        resize(imgPath, imgName, size1920, '1920')
                        resize(imgPath, imgName, size800, '800')
                        resize(imgPath, imgName, sizeThumb, 'thumbs')
                # for dirInfo in dirs[1]:
                #     fdName = handleFolderName(dirInfo)

                #     if fdName != '':
                #         created_at = handleCreatedAt(fdName)
                #         for img in dirInfo[2]:
                #             if img not in ignore_img:
                #                 content = "/source/{}/{}".format(dirInfo[0].replace("../", ""), img)
                #                 imgName = hashlib.md5(content.encode('utf-8')).hexdigest()
                #                 imgPath = "{}/{}".format(dirInfo[0], img)
                #                 thumb = imgName+".png"
                #                 # resize(imgPath, imgName, size1920, '1920')
                #                 # resize(imgPath, imgName, size800, '800')
                #                 # resize(imgPath, imgName, sizeThumb, 'thumbs')
                #                 payload = json.dumps({
                #                     "title": imgName,
                #                     "slug": imgName,
                #                     "thumb": thumb,
                #                     "content": content,
                #                     "excerpt": git_link,
                #                     "created_at": str(created_at)
                #                 })
                #                 # insert(payload)


insertImg()
