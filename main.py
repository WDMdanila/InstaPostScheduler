import os
import time
import json
from instabot import Bot

with open("config.json", "r") as f:
    data = json.load(f)

i, n = 0, 0
text = [[]]

with open(data['text_file'], "r") as f:
    lines = f.readlines()
    for line in lines:
        if line != "\n":
            text[n].append(line.strip())
        if line == "\n":
            text[n] = '\n'.join(text[n])
            text.append([])
            n += 1
    text[n] = '\n'.join(text[n])

filenames = os.listdir(data['images_dir'])
filenames.sort()
timer = int(float(data['time_sleep'])*60)

bot = Bot()
bot.login(username=data['login'],
          password=data['password'])
while True:
    i += 1
    bot.upload_photo(f"{data['images_dir']}/{filenames[i-1]}", caption=text[i-1])
    time.sleep(timer)
    if i == min(len(text), len(filenames)):
        break

bot.logout()
