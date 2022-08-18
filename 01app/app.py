from tkinter.font import names
from unicodedata import name
from insert import insert
import json
import os
import hashlib
from datetime import datetime


ignore_folder = ['.git', '01app']
git_link = "https://raw.githubusercontent.com/phobrv/tep/main"
print(hashlib.md5("whatever your string is".encode('utf-8')).hexdigest())


def handleFolderName(name: str):
    return name.replace("../", "").split("/")[0]


def handleCreatedAt(createStr: str):
    nameSplit = createStr.split(",")
    if(len(nameSplit) > 2):
        createStr = "{}, {}".format(nameSplit[-2].strip(), nameSplit[-1].strip())
    createStr = datetime.strptime(createStr, "%B %d, %Y")
    return createStr


for dirInfo in os.walk('../'):
    fdName = handleFolderName(dirInfo[0])
    if fdName not in ignore_folder and fdName != '':
        created_at = handleCreatedAt(fdName)
        for img in dirInfo[2]:
            thumb = "/{}/{}".format(dirInfo[0].replace("../", ""), img)
            title = hashlib.md5(thumb.encode('utf-8')).hexdigest()
            payload = json.dumps({
                "title": title,
                "slug": title,
                "thumb": thumb,
                "excerpt": git_link,
                "created_at": str(created_at)
            })
            insert(payload)
