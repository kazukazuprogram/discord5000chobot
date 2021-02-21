#!/usr/bin/env python3
# coding: utf-8

from PIL import Image, ImageDraw


def splitarg(s):
    words = list()
    tmpw = ""
    in_quota = False
    for w in s.split():
        if '"' not in w and not in_quota:
            words.append(w)
        elif '"' in w and w[w.index('"')-1] == "\\":
            words.append(w)
        else:
            if '"' in w and w[w.index('"')-1] == "\\":
                tmpw += " " + w
            elif w[-1] == '"':
                tmpw += " " + w[:-1]
                words.append(tmpw)
                tmpw = ""
                in_quota = False
            elif in_quota:
                tmpw += " " + w
            elif w[0] == '"':
                tmpw = ""
                tmpw += w[1:]
                in_quota = True
    return words


def getTextWidth(text, font, width=100, height=500, recursive=False):
    step = 100
    img = Image.new("L", (width, height))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, font=font, fill=255)
    box = img.getbbox()
    if box[2] < width-step or (recursive and box[2] == width-step):
        return box[2]
    else:
        return getTextWidth(text=text, font=font, width=width+step, height=height, recursive=True)
