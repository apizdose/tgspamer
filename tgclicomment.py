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
channel = client.get_entity('linux_gram')
messages = client.get_messages(channel, limit= 5)

msg_ids=[]

for i in messages:
    msg_ids.append(i.id)

print(msg_ids)    
ranid=msg_ids[random.randint(0,len(msg_ids)-1)]

client.send_message(channel, 'wow', comment_to=ranid)




