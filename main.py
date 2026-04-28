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

    # Reaction Log (Only logs reactions to messages sent during runtime)
    async def on_reaction_add(self, reaction, user):
        with open(f'{reaction.message.channel}.txt','a') as file:
            file.write(f'{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {user} (ID = {user.id}):\n')
            file.write(f'\tReacted {reaction} to: {reaction.message.content}\n')

    async def on_reaction_remove(self,reaction,user):
        with open(f'{reaction.message.channel}.txt','a') as file:
            file.write(f'{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {user} (ID = {user.id}):\n')
            file.write(f'\tRemoved reaction {reaction} to: {reaction.message.content}\n')


    # Edit Log

    async def on_message_edit(self,before,after):
        with open(f'{before.channel}.txt','a') as file:
            file.write(f'{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {before.author} (ID = {before.author.id}):\n')
            file.write(f'\tEdited {before.content} to {after.content}\n')
 

client = MyClient(chunk_guilds_at_startup=False)
client.run(token)

