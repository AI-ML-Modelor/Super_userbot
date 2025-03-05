from pyrogram import Client, idle
import onewordraid  # Ensure karo ki yeh sahi path pe ho

API_ID = 1234567  # Apna API ID daalo
API_HASH = "your_api_hash_here"
SESSION_NAME = "your_session_name"

M = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

M.add_handler(plugins.onewordraid.start_raid)
M.add_handler(plugins.onewordraid.stop_raid)

M.start()
print("Bot Started Successfully")
idle()
M.stop()
