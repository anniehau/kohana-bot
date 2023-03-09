import textwrap
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        bot_creator_id = "298249837965606912"
        message_to_send = textwrap.dedent(
            f"""\
                **I'm a discord bot made by <@{bot_creator_id}>!**

                :notebook: **My available commands are:**
                > **!about**
                > * Tells you more about myself and my commands.

                > **!clean n** *
                > * Clears n amout of messages from the current channel. Default is 100.
                * *Admin only.*

                *I can't do much right now, but I hope you'll support me as I grow!!*
            """
        )
        await ctx.send(message_to_send)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx):
        user_input = ctx.message.content[7:]
        limit = int(user_input) if user_input.isdigit() else 100
        removed = await ctx.channel.purge(limit=limit)

        message_to_send = textwrap.dedent(
            f"""\
                *Channel cleaned, it's now all new and shiny!* :broom:
                > A total of **{len(removed)}** messages were removed.
                > Message clean limit was **{limit if limit != 100 else f"default ({limit})"}**.
            """
        )
        await ctx.send(message_to_send)
