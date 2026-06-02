from setuptools import setup, find_packages

setup(
    name='DiscordScraper',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'discord.py-self[voice]>=2.1.0',
        'Click'
    ],
    entry_points={
        'console_scripts': [
            'discordscraper=DiscordLogger.main:run_bot',
            'ds=DiscordLogger.main:run_bot',
            'discordscraper --parent=DiscordLogger.main:get_dir',
            'ds -p=DiscordLogger.main:get_dir',
            'discordscraper --setup=DiscordLogger.main:setup',
            'ds -s=DiscordLogger.main:setup',
            'discordscraper --update-token=DiscordLogger.main:update_token',
            'discordscraper --update-directory=DiscordLogger.main:update_directory'
        ]
    },
    author='Aiden Deane',
    author_email='Aiden.Deane@me.com',
)