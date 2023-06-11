#!/usr/bin/env python3
# telegram bot that sends a video


import os
import json
import telegram
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    #bot = telegram.Bot(os.getenv('TELEGRAM_TOKEN'))
    bot = telegram.Bot(os.getenv('TELEGRAM_TOKEN'), base_url=os.getenv('TELEGRAM_API_URL'))
    async with bot:
        #print(await bot.get_me())
        # print((await bot.get_updates())[0])

        msg = json.dumps(dict(os.environ), indent=4)
        if os.getenv("sonarr_eventtype") == "Test":
            await bot.send_message(text = "im a test", chat_id=os.getenv('CHAT_ID'))
        elif os.getenv("sonarr_eventtype") == "Download":
            await bot.send_message(text=f"Series: {os.getenv('sonarr_series_title')} Episode {os.getenv('sonarr_episodefile_episodenumbers')}", chat_id=os.getenv('CHAT_ID'))
            await bot.send_video(video=open('./light_test.mp4', 'rb'), chat_id=os.getenv('CHAT_ID'), supports_streaming=True,
                             write_timeout=10000, read_timeout=10000, connect_timeout=1000)
            #await bot.send_video(video=open(os.getenv('sonarr_episodefile_path'), 'rb'), chat_id=os.getenv('CHAT_ID'))
        else:
            print(os.getenv('CHAT_ID'))
            await bot.send_message(text="im an un handled event", chat_id=os.getenv('CHAT_ID'))

        


if __name__ == '__main__':
    asyncio.run(main())
