# Main executor file

from discord import *
import tomllib
import os
import pathlib
import time

program_dir = pathlib.Path(__file__).resolve().parent

def setup():
    token = input("Enter the static token:\n> ")
    working_directory = input("Enter the parent directory you wish to log files to:\n> ")
    file = open(f'{program_dir}/config.toml','w')
    file.write(f'token = "{token}"\nworking_directory = "{working_directory}"')
    file.close()
    
    # Create necessary dirs

    pathlib.Path(f'{working_directory}/DiscordScraper/message_logs').mkdir(exist_ok=True)
    pathlib.Path(f'{working_directory}/DiscordScraper').mkdir(exist_ok=True)

def get_dir():
    print(pathlib.Path(__file__).resolve().parent)

def run_bot():
    if not pathlib.Path(f'{program_dir}/config.toml').is_file():
        return print('Config file missing. Please run the initial setup command.')
    else:
        working_directory = f"{tomllib.load(open(f'{program_dir}/config.toml','rb'))['working_directory']}/DiscordScraper"
        class MyClient(Client):
            async def on_ready(self):
                print('Logged on as', self.user)

            async def on_message(self, message):
                print('Message',message,'recieved.')

                pathlib.Path(f'{working_directory}/message_logs/{message.guild}').mkdir(exist_ok=True)  # Creates working_directory for server message was sent in
                os.chdir(f'{working_directory}/message_logs/{message.guild}')
                print(os.getcwd())
                
                if message.attachments != []:
                    if isinstance(message.attachments[0],Attachment) and message.attachments: # Check
                        for sent_attachment in message.attachments:
                            with open(f'{message.channel}.txt','a+') as file:
                                file.write(f"{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {message.author} (User ID = {message.author.id}):\n")
                                file.write(f'\tSent attachment: {sent_attachment.url}\n')
                                file.write(f'\tMessage ID {message.id}\n')

                # Log text messages
                with open(f'{message.channel}.txt','a') as file:
                    file.write(f"{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {message.author} (User ID = {message.author.id}):\n")
                    file.write(f'\t{message.content}\n')

                # Reaction Log (Only logs reactions to messages sent during runtime)
            async def on_reaction_add(self, reaction, user):

                pathlib.Path(f'{working_directory}/message_logs/{reaction.message.guild}').mkdir(exist_ok=True)  # Creates working_directory for server message was sent in
                os.chdir(f'{working_directory}/message_logs/{reaction.message.guild}')

                with open(f'{reaction.message.channel}.txt','a') as file:
                    file.write(f"{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {user} (User ID = {user.id}):\n")
                    if reaction.message.content != '':
                        file.write(f'\tReacted {reaction} to: {reaction.message.content}\n')
                    else:
                        file.write(f'\tReacted {reaction} to attachment\n')
                    
                    file.write(f'\tMessage ID: {reaction.message.id}\n')

            async def on_reaction_remove(self,reaction,user):

                pathlib.Path(f'{working_directory}/message_logs/{reaction.message.guild}').mkdir(exist_ok=True)  # Creates working_directory for server message was sent in
                os.chdir(f'{working_directory}/message_logs/{reaction.message.guild}')

                with open(f"{reaction.message.channel}.txt','a'") as file:
                    file.write(f"{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {user} (User ID = {user.id}):\n")
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
                    file.write(f"{time.strftime('%d/%m/%Y - %H:%M',time.localtime())} {before.author} (User ID = {before.author.id}):\n")
                    file.write(f'\tEdited {before.content} to {after.content}\n')

        client = MyClient(chunk_guilds_at_startup=False)
        client.run(tomllib.load(open(f'{program_dir}/config.toml','rb'))['token'])