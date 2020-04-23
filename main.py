import os
import time
import json
from instabot import Bot

with open("config.json", "r") as f:
    data = json.load(f)

if 'login' not in data or 'password' not in data:
    raise AttributeError('Login information is needed')
if 'text_file' not in data:
    raise AttributeError('text_file must be specified')
if 'images_dir' not in data:
    raise AttributeError('images_dir must be specified')
if 'time_sleep' not in data:
    raise AttributeError('time_sleep must be specified')
if float(data['time_sleep']) < 0:
    raise AttributeError('time_sleep can not be negative!')


timer = int(float(data['time_sleep'])*60)

n = 0
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

bot = Bot()
bot.login(username=data['login'],
          password=data['password'])
n = 0
while True:
    n += 1
    bot.upload_photo(f"{data['images_dir']}/{filenames[n-1]}", caption=text[n-1])
    time.sleep(timer)
    if n == min(len(text), len(filenames)):
        break

bot.logout()
