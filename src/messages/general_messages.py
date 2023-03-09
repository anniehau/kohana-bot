import textwrap


def get_about_message():
    bot_creator_id = "298249837965606912"
    return textwrap.dedent(
        f"""\
            **I'm a discord bot made by <@{bot_creator_id}>!**

            :notebook: **My available commands are:**
            > **!about**
            > * Tells you more about myself and my commands.

            > **!clean n** *
            > * Clears n amout of messages from the current channel. Default is 100.
            * *Admin only.*

            > **!silent_clean** *
            > * Clears the last 100 messages from the channel without returning anything.
            * *Admin only.*

            *I can't do much right now, but I hope you'll support me as I grow!!*
        """
    )


def get_clean_message(limit, removed):
    return textwrap.dedent(
        f"""\
            *Channel cleaned, it's now all new and shiny!* :broom:
            > A total of **{len(removed)}** messages were removed.
            > Message clean limit was **{limit if limit != 100 else f"default ({limit})"}**.
        """
    )
