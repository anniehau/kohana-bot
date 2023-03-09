from discord.ext import commands
from discord.utils import get


class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = get(member.server.roles, name="🐈")
        member.add_roles(member, role)
