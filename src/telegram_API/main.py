import asyncio
import os
from dotenv import load_dotenv
from telethon import TelegramClient

os.environ.clear()
load_dotenv(override=True)

TELEGRAM_API_ID = os.environ.get('TELEGRAM_API_ID')
TELEGRAM_API_HASH =os.environ.get('TELEGRAM_API_HASH')
async def main():
  
     client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)
     await client.start()
     await client.send_message('me', 'Hello, myself!')
     return

asyncio.run(main())