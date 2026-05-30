from setuptools import setup, find_packages

setup(
    name='DiscordLogger',
    version='0.5.2',
    packages=find_packages(),
    install_requires=[
        'discord.py-self[voice]>=2.1.0'
    ],
    entry_points={
        'console_scripts': [
            'discord-logger=DiscordLogger.main:main'
        ]
    },
)