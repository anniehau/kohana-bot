from discord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            message_to_send = "*Sorry... I couldn't understand your command...* <:ff14_cry:1083469495080849468>"
            return await ctx.send(message_to_send)

        print(error)
