from setuptools import setup, find_packages

setup(
    name='DiscordScraper',
    version='1.0.22',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'discord.py-self[voice]>=2.1.0'
    ],
    entry_points={
        'console_scripts': [
            'discord-logger=DiscordLogger.main:run_bot',
            'update-token=DiscordLogger.main:update_token',
            'dl-dir=DiscordLogger.main:get_dir'
        ]
    },
    author='Aiden Deane',
    author_email='Aiden.Deane@me.com',
)