import os
from dotenv import load_dotenv
from src import config
from src.client import Client


# Loads global variables
load_dotenv()
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")


async def run():
    intents = config.get_intents()

    bot = Client(command_prefix=PREFIX, intents=intents)
    await config.setup_cogs(bot)

    await bot.start(TOKEN)
