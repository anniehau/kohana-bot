from discord.ext import commands
from src.messages import general_messages


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        bot_creator_id = "298249837965606912"
        message_to_send = general_messages.get_about_message()
        await ctx.send(message_to_send)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx):
        user_input = ctx.message.content[7:]
        limit = int(user_input) if user_input.isdigit() else 100
        removed = await ctx.channel.purge(limit=limit)

        message_to_send = general_messages.get_clean_message(limit, removed)
        await ctx.send(message_to_send)
