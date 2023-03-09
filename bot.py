import os
import textwrap
import discord
from discord.ext import commands
from dotenv import load_dotenv
import config
import math


# Loads global variables
load_dotenv()


# Constants
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")


def run_bot():
    intents = config.get_intents()
    bot = commands.Bot(command_prefix=PREFIX, intents=intents)

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Game("with Yumi 🐩"))
        print(f"{bot.user} has woken up!")

    @bot.command()
    async def about(ctx):
        bot_creator_id = "298249837965606912"
        message_to_send = textwrap.dedent(
            f"""\
                I'm a discord bot made by <@{bot_creator_id}>!
                I can't do much right now, but I hope you'll support me as I grow!!!
            """
        )
        await ctx.send(message_to_send)

    @bot.command()
    async def clean(ctx):
        user_input = ctx.message.content[7:]
        limit = int(user_input) if user_input.isdigit() else 100
        removed = await ctx.channel.purge(limit=limit)

        message_to_send = textwrap.dedent(
            f"""\
                *Channel cleaned, it's now all new and shiny!* :broom:
                > A total of **{len(removed)}** messages were removed.
                > Message clean limit was **{limit if limit is not 100 else f"default ({limit})"}**.
            """
        )
        await ctx.send(message_to_send)

    bot.run(TOKEN)
