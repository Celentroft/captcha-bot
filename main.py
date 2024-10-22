# Dev by celentroft aka scarlxrd_1337
# Github: https://github.com/Celentroft
# Portfolio: https://scarlxrd-developer.vercel.app/
# Update comming soon x) 

import os
import discord
from functions import load_json
from discord.ext import commands

config = load_json()

async def load_files(bot) -> None:
    commands_files = [f'commands.{filename[:-3]}' for filename in os.listdir('./commands/') if filename.endswith('.py')]
    # events_files = [f'events.{filename[:-3]}' for filename in os.listdir('./events/') if filename.endswith('.py')]
    for file in commands_files:
        try:
            await bot.load_extension(file)
        except Exception as e:
            print(e)
            
    # for file in events_files:
    #     try:
    #         await bot.load_extension(file)
    #     except Exception as e:
    #         print(e)

class MyBot(commands.Bot):
    def __init__(self) -> None:
        self.config = load_json()
        super().__init__(
            intents=discord.Intents.all(),
            command_prefix="scarlxrd",
            help_command=None
        )
        
    async def on_ready(self) -> None:
        await load_files(self)
        await self.tree.sync()
        print(f"Connecter en tant que {self.user.name}")
        print("Github: https://github.com/Celentroft")
        print("Telegram: https://t.me/scarlxrd_1337")
        
Bot = MyBot()
Bot.run(config['token'])