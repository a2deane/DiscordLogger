from setuptools import setup, find_packages

setup(
    name='DiscordScraper',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'discord.py-self[voice]>=2.1.0'
    ],
    entry_points={
        'console_scripts': [
            'discord-logger=DiscordLogger.main:run_bot',
            'update-token=DiscordLogger.main:update_token'
        ]
    },
)