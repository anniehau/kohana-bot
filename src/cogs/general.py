from discord.ext import commands
from src.messages import general_messages


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        message_to_send = general_messages.get_about_message()
        await ctx.send(message_to_send)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx):
        limit = self.validate_clean_content(ctx.message.content)
        removed = await ctx.channel.purge(limit=limit)
        message_to_send = general_messages.get_clean_message(limit, removed)
        await ctx.send(message_to_send)

    def validate_clean_content(self, content):
        user_input = content[7:]
        return int(user_input) if user_input.isdigit() else 100
