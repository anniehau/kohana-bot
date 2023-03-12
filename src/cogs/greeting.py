from discord.ext import commands
from discord.utils import get


class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = get(member.guild.roles, id=1055657900632186940)
        await member.add_roles(role)
