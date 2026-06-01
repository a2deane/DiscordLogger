# Main executor file

from discord import *
import tomllib
import os
import pathlib
import time

working_directory = f"{pathlib.Path('main.py').resolve().parent}/DiscordLogger"

def get_dir():
    return print(working_directory)
    
def update_token():
    new_token = input('Enter static token:\n> ')
    file = open('config.toml','w')
    file.write(
        f'token = "{new_token}"\ntoken_inserted = "True"'
    )
    return print('Token updated successfully.')

def update_directory():
    new_directory = input('Enter the directory you wish to serve files to')
    try:
        pathlib.Path(f'{new_directory}/DiscordScraper').mkdir()
        print('Created folder "DiscordScraper" at desired path')
    except OSError:
        print('Invalid path')

def run_bot():
    if not tomllib.load(open(f'{working_directory}/config.toml','rb'))['token_inserted']:
        print('Token not inserted. Insert before starting bot.')
        return
    else:
        class MyClient(Client):
            async def on_ready(self):
                print('Logged on as', self.user)

            async def on_message(self, message):

                pathlib.Path(f'{working_directory}/message_logs/{message.guild}').mkdir(exist_ok=True)  # Creates working_directory for server message was sent in
                os.chdir(f'{working_directory}/message_logs/{message.guild}')

        client = MyClient(chunk_guilds_at_startup=False)
        client.run(tomllib.load(open('DiscordLogger/config.toml','rb'))['token'])

