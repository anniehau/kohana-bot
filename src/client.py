import os
import discord
from discord.ext import commands


class Client(commands.Bot):
    async def on_ready(self):
        await self.change_presence(activity=discord.Game("with Yumi 🐩"))
        print(f"{self.user} has woken up!")
