# Main executor file

from discord import *
import os
import pathlib
import time
from config import token
from config import working_directory


class MyClient(Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):

        pathlib.Path(f'{working_directory}/message_logs/{message.guild}').mkdir(exist_ok=True)  # Creates working_directory for server message was sent in
        os.chdir(f'{working_directory}/message_logs/{message.guild}')

        if message.attachments != []:
            if isinstance(message.attachments[0],Attachment) and message.attachments: # Check
                for sent_attachment in message.attachments:
                    with open(f'{message.channel}.txt','a') as file:
                        file.write(f'{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {message.author} (User ID = {message.author.id}):\n')
                        file.write(f'\tSent attachment: {sent_attachment.url}\n')
                        file.write(f'\tMessage ID {message.id}\n')

        # Log text messages
        with open(f'{message.channel}.txt','a') as file:
            file.write(f'{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {message.author} (User ID = {message.author.id}):\n')
            file.write(f'\t{message.content}\n')

    # Reaction Log (Only logs reactions to messages sent during runtime)
    async def on_reaction_add(self, reaction, user):

        pathlib.Path(f'{working_directory}/message_logs/{reaction.message.guild}').mkdir(exist_ok=True)  # Creates working_directory for server message was sent in
        os.chdir(f'{working_directory}/message_logs/{reaction.message.guild}')

        with open(f'{reaction.message.channel}.txt','a') as file:
            file.write(f'{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {user} (User ID = {user.id}):\n')
            if reaction.message.content != '':
                file.write(f'\tReacted {reaction} to: {reaction.message.content}\n')
            else:
                file.write(f'\tReacted {reaction} to attachment\n')
            
            file.write(f'\tMessage ID: {reaction.message.id}\n')

    async def on_reaction_remove(self,reaction,user):

        pathlib.Path(f'{working_directory}/message_logs/{reaction.message.guild}').mkdir(exist_ok=True)  # Creates working_directory for server message was sent in
        os.chdir(f'{working_directory}/message_logs/{reaction.message.guild}')

        with open(f'{reaction.message.channel}.txt','a') as file:
            file.write(f'{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {user} (User ID = {user.id}):\n')
            if reaction.message.content != '':
                file.write(f'\tRemoved reaction {reaction} from {reaction.message.content}\n')
            else:
                file.write(f'\tRemoved reaction {reaction} from attachment\n')
            file.write(f'\tMessage ID: {reaction.message.id}\n')

    # Edit Log

    async def on_message_edit(self,before,after):


        pathlib.Path(f'{working_directory}/message_logs/{before.message.guild}').mkdir(exist_ok=True)  # Creates working_directory for server message was sent in
        os.chdir(f'{working_directory}/message_logs/{before.message.guild}')


        with open(f'{before.channel}.txt','a') as file:
            file.write(f'{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {before.author} (User ID = {before.author.id}):\n')
            file.write(f'\tEdited {before.content} to {after.content}\n')
 

client = MyClient(chunk_guilds_at_startup=False)
client.run(token)

