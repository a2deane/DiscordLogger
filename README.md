# DiscordLogger

## About
DiscordLogger is a screen-scraping Discord Self-Bot, built with the Discord.py-Self API with voice functionality. 
This project aims to log messages, reactions, edits, attachments (via Discord CDN URL), and voice conversations.

## What works
Text, reaction, edit, and image attachment logging currently works.

## Future plans
I plan to implement voice call recording.

## Important information
It shall be noted that self-bots are against Discord's TOS. As such, it is recommended that you do not use your personal account to run the self-bot, but rather, an alternative account.

## Dependencies
In order to run this package, [``discord.py-self[voice]``](https://discordpy-self.readthedocs.io/en/latest/intro.html) must be installed in the same folder as the main, and config py files.

## Running the Program
Ensure that the account token for which you are logging from is pasted into the ``config.py`` file. (You may need to run the ``config.py`` file to update the token)

Since this is a CLI tool, you simply execute ``python main.py`` in your system terminal in order to execute the program.

Logged message data is stored in the form of a .txt file under the appropriately named ``message_logs`` directory.
