import asyncio
import os
from dotenv import load_dotenv
from telethon import TelegramClient

# Load environment variables
load_dotenv(override=True)

# You can use new environment variables here if you have a second API set
# e.g., os.environ.get('NEW_TELEGRAM_API_ID')
API_ID = os.environ.get('TELEGRAM_API_ID')
API_HASH = os.environ.get('TELEGRAM_API_HASH')

async def main():
    # Using a different session name for this new client instance
    client = TelegramClient('new_api_session', API_ID, API_HASH)
    
    print("Connecting to Telegram...")
    await client.start()
    
    # Get information about the signed-in user
    me = await client.get_me()
    print(f"Successfully connected with new session!")
    print(f"User: {me.first_name} {me.last_name or ''}")
    print(f"ID: {me.id}")
    print(f"Phone: {me.phone}")
    
    # Example: List existing dialogs (chats)
    print("\nRecent chats:")
    async for dialog in client.iter_dialogs(limit=5):
        print(f"- {dialog.name} (ID: {dialog.id})")

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
