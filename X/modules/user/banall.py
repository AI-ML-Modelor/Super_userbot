from asyncio import sleep
from pyrogram import Client, filters
from pyrogram types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from pyrogram.functions.channels import EditBannedRequest
from config import OWNER_ID, CMD_HANDLER
error = []

@Client.on(admin_cmd(pattern=r"banall", outgoing=True))
async def testing(event):
    global error
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("**𝒀𝒐𝒖 𝑫𝒐𝒏❜𝒕 𝒉𝒂𝒗𝒆 𝑺𝒖𝒇𝒇𝒊𝒄𝒊𝒆𝒏𝒕 𝑹𝒊𝒈𝒉𝒕𝒔**")
        return
    await event.edit("**Dᴏɪɴɢ Nᴏᴛʜɪɴɢ 🙃🙂**")
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
        except Exception as e:
            error.append(str(e))
            pass
    await event.edit("**Nᴏᴛʜɪɴɢ Hᴀᴘᴘᴇɴᴇᴅ Hᴇʀᴇ 🙃🙂**")
    print (error)

add_command_help(
    "•─╼⃝𖠁 ʙᴀɴᴀʟʟ",
    [
        ["banall", "Tᴏ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀ ɪɴ ᴛʜɪꜱ ᴄʜᴀᴛ."],
    ],
)