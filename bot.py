import discord
from handlers import messages


def get_intents():
    intents = discord.Intents.default()
    intents.message_content = True
    return intents


def run_bot(token):
    intents = get_intents()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} has woken up!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        await messages.handle_message(message)

    client.run(token)
