import os
from dotenv import load_dotenv
import bot


# Loads global variables
load_dotenv()


# Constants
TOKEN = os.getenv("TOKEN")


if __name__ == "__main__":
    load_dotenv()
    bot.run_bot(TOKEN)
