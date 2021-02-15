#!/usr/bin/env python3
# coding: utf-8

from .genimg import genImage, genBaseImage, _round
from .utils import splitarg
from discord import Client, Game, File
from os import environ
from io import BytesIO

client = Client()
width = 1500
height = 500
base = genBaseImage(width=width, height=_round(height/2))


@client.event
async def on_ready():
    print("Logged in.")
    await client.change_presence(activity=Game(name='Running'))


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if len(message.content) != 0:
        mes = splitarg(message.content)
        print(mes)
        if mes[0] == "!5000":
            if len(mes) == 1:
                await message.channel.send('引数を指定してください')
            else:
                if len(mes) <= 2:
                    img = genImage(mes[1], max_width=width, height=height, base=base)
                elif len(mes) >= 3:
                    img = genImage(mes[1], mes[2], max_width=width, height=height, base=base)
                fp = BytesIO()
                img.save(fp, format="png")
                fp.seek(0)
                await message.channel.send("", file=File(fp, filename="bot.png"))


def main():
    client.run(environ["TOKEN"])


if __name__ == "__main__":
    main()
