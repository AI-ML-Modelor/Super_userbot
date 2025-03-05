import asyncio
from pyrogram import Client, filters

# One-word spam ke words
WORDS = ["word1", "word2", "word3"]

# Flood wait control (seconds me)
DELAY_BETWEEN_MESSAGES = 0.1

# Raid ka status track karne ke liye
raid_active = False

@Client.on_message(filters.command(["T3R1", "LOL", "AJA", "AAJA", "START"]) & filters.me)
async def start_raid(client, message):
    global raid_active
    if raid_active:
        await message.reply_text("YE RANDI KA PILLA PEHLE HI CHUDD RAHA HAI")
        return

    raid_active = True
    await message.reply_text("AB TOH ISKI MAA CHODDOONGA MAI")

    while raid_active:
        for word in WORDS:
            if not raid_active:
                break
            await message.reply_text(word)
            await asyncio.sleep(DELAY_BETWEEN_MESSAGES)

@Client.on_message(filters.command(["XD", "FARAR", "STOP", "FUCKED"]) & filters.me)
async def stop_raid(client, message):
    global raid_active
    if not raid_active:
        await message.reply_text("RANDI CHUDDRHA HAI CHORR DOO USE")
        return

    raid_active = False
    await message.reply_text("MAA CHUDD GYI ISKI TOH😂")
