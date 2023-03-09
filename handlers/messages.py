import textwrap


async def handle_message(message):
    if message.content[0] == "?":
        return await handle_commands(message)


async def handle_commands(message):
    if message.contet == "?help":
        return await help_command(message)


async def help_command(message):
    bot_creator_id = "298249837965606912"
    message_to_send = textwrap.dedent(
        f"""\
            I'm a discord bot made by <@{bot_creator_id}>!
            I can't do much right now, but I hope you'll support me as I grow!!!
        """
    )

    return await message.channel.send(message_to_send)
