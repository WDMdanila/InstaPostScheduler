import json
import time
from instabot import Bot

with open("config.json", "r") as f:
    data = json.load(f)

i, n = 0, 0
text = [[]]

with open("text.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        if line != "\n":
            text[n].append(line.strip())
        if line == "\n":
            text[n] = '\n'.join(text[n])
            text.append([])
            n += 1
    text[n] = '\n'.join(text[n])

bot = Bot()
bot.login(username=data['login'],
          password=data['password'])

while True:
    print(i)
    bot.upload_photo(f"images/{i}.jpg", caption=text[i-1])
    time.sleep(2)
    if i == len(text):
        break
