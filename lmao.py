from telethon import TelegramClient
from unsyncedpieceofsh import API_ID, API_HASH, groups
from datetime import timedelta
import random


#im letting them stay here because why not
#API_ID = 1234567890#your_fucking_apiID
#API_HASH = '1234567890abcdefghijk'
#groups = ["your_groups_ID","you_stupid_fuck"]
defaultmirko = 'mirko '

client = TelegramClient('lmao', API_ID, API_HASH)

with open("lmao.txt") as f:
    templmao = f.readline()
    lmao = templmao.split()
lmaoL = len(lmao)


async def main():
    for selgroup in groups:

        c = random.randint(3,12)
        str = ''
        for a in range(1,c):
            b = random.randint(0,lmaoL)
            if a == int(c/2) :
                str += defaultmirko
            str = ''.join([str, lmao[b] ,' '])

        await client.send_message(selgroup, str, schedule=timedelta(seconds=random.randint(3,10)))

if __name__ == "__main__":
    with client:
       client.loop.run_until_complete(main())
