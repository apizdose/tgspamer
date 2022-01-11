from telethon import TelegramClient, events, sync
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest
import time
import asyncio
import random

api_id = 
api_hash = ''

client = TelegramClient('session_name', api_id, api_hash)
client.start('')

chats = []

with open ('tgbase.txt','r',encoding='utf-8') as file:
    for i in file:
        chats.append(i[:-1])

def ChatId(arr):
    i=0
    while True:
        yield arr[i]
        i+=1
        if i == len(arr):
            i=0
            
chatid = ChatId(chats)

message=['Looking for boyfriend.', 'Boys, DM me!', 'wanna see my naked photos?','Looking for free $@X! DM!', 'Hi guys, who wanna chat?']
message_rus=['Познакомлюсь, давно не было парня.','Хочешь увидеть мои фото? ЛС.','Мужчины, пишите. Скучаю!', 'Как хочется настоящего мужчину']

async def post_msg():
    chatscount=0
    while True:
        chatscount += 1
        if chatscount >= 300:
            async for dialog in client.iter_dialogs():
                await dialog.delete()
        randsleep=random.randint(3,6)
        cyrillic=False
        chat_id=next(chatid)
        await asyncio.sleep(randsleep)
        try:
            about = await client(GetFullChannelRequest(channel=chat_id))
            for i in russ:
                if i in about.full_chat.about:
                    cyrillic=True
            await client(JoinChannelRequest(chat_id))
        except:
            print('Error join chat!')
        message_text=message[random.randint(0,(len(message)-1))]    
        if cyrillic:
            message_text=message_rus[random.randint(0,(len(message_rus)-1))]
        
            
        try:
            
            #await client.send_message(chat_id,message_text)
            print('----------------------------------Sended: '+chat_id)
            with open('chats_good.txt','a',encoding='utf-8') as logerfile:
                logerfile.write(chat_id+'\n')
                
        except Exception as ex:
            print('Error message!')


@client.on(events.NewMessage(incoming=True))
async def handle_incoming_message(event):
    
    
    await asyncio.sleep(5)
    if event.is_private:
        await event.respond("Hi, let's go ... ")

with client:
    client.loop.run_until_complete(post_msg())

