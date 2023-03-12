import discord
from src.cogs.error_handler import ErrorHandler
from src.cogs.greeting import Greeting
from src.cogs.general import General
from src.cogs.color_picker import ColorPicker


def get_intents():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.reactions = True
    return intents


async def setup_cogs(bot):
    await bot.add_cog(Greeting(bot))
    await bot.add_cog(General(bot))
    await bot.add_cog(ErrorHandler(bot))
    await bot.add_cog(ColorPicker(bot))
