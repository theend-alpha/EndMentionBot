from pyrogram import Client as teletips, filters
from pyrogram.types import Message
from Database.users import *

@teletips.on_message(group=1)
async def cwf(_, m):
    if m.chat.type == "private":
        return
    if is_served_chat(m.chat.id):
        return
    add_chat(m.chat.id)

@teletips.on_message(filters.text)
async def pcwf(_, m):
    if m.chat.type == "private":
        if is_served_user(m.chat.id):
            return
        add_user(m.chat.id)

@teletips.on_message(filters.command("stats") & filters.user(1985209910))
async def stats(_, m: Message):
    chats = list_chats()
    users = list_users()
    CHATS = []
    USERS = []
    for chat in chats:
        CHATS.append(chat.chat_id)
    for user in users:
        USERS.append(user.id)
    lel = ""
    for CHAT in CHATS:
        chat = str(CHAT)
        lel += f"\n<code>{chat}</code>"
    lmao = ""
    for USER in USERS:
        user = str(USER)
        lmao += f"\n<code>{user}</code>"
    await m.reply(f"**Served chats** :-\n{lel}\n\n**Count** :- {len(CHATS)}\n\n**Users** :-\n{lmao}\n\n**Count** :- {len(USERS)}")
