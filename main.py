# Main executor file

import discord
import os
import pathlib
import time
from config import token
from config import directory

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):

        if message.content == 'ping':
            await message.channel.send('pong')

        # Log messages

        pathlib.Path(f'{directory}/message_logs/{message.guild}').mkdir(exist_ok=True)  # Create new directory for server

        os.chdir(f'{directory}/message_logs/{message.guild}')
        with open(f'{message.channel}.txt','a') as file:
            file.write(f'{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {message.author} (ID = {message.author.id}):\n')
            file.write(f'\t{message.content}\n')

client = MyClient(chunk_guilds_at_startup=False)
client.run(token)
