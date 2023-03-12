from discord.ext import commands
from discord.utils import get
from src.messages import general_messages


class ColorPicker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        is_role_message = await self.validate_message(payload)
        if is_role_message:
            role_name = payload.emoji.name.capitalize()
            role = get(payload.member.guild.roles, name=role_name)
            await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        is_role_message = await self.validate_message(payload)
        if is_role_message:
            guild = get(self.bot.guilds, id=payload.guild_id)
            member = get(guild.members, id=payload.user_id)
            role_name = payload.emoji.name.capitalize()
            role = get(member.guild.roles, name=role_name)
            await member.remove_roles(role)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def set_role_picker(self, ctx):
        message_to_send = general_messages.get_roles_message()
        message = await ctx.send(message_to_send)
        await message.add_reaction("<:red:1084340345489346560>")
        await message.add_reaction("<:orange:1084340341232119808>")
        await message.add_reaction("<:yellow:1084340346940563547>")
        await message.add_reaction("<:green:1084340340028346478>")
        await message.add_reaction("<:blue:1084340337859907594>")
        await message.add_reaction("<:purple:1084340344163946686>")
        await message.add_reaction("<:pink:1084340341982892133>")

    async def validate_message(self, payload):
        roles_message = general_messages.get_roles_message()
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        return message.content == roles_message
