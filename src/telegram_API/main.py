import asyncio
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

os.environ.clear()
load_dotenv(override=True)

TELEGRAM_API_ID = os.environ.get('TELEGRAM_API_ID')
TELEGRAM_API_HASH =os.environ.get('TELEGRAM_API_HASH')
async def main():
     
     client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)
     @client.on(events.NewMessage)
     async def handle_message(event):
           print(event.message.text)
           await event.reply(event.message.text)
     await client.start()
     await client.send_message('me', 'Hello, myself!')
     await client.run_until_disconnected()
     return handle_message

asyncio.run(main())