from discord.ext import commands
from src.messages import error_messages


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            message_to_send = error_messages.get_unknown_command_message()
            return await ctx.send(message_to_send)
        print(error)
