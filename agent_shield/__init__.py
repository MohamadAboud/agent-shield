# """ Third-party modules """
import click
from dotenv import load_dotenv

# """ Local modules """
import agent_shield.commands as commands


# Load the environment variables from the .env file
load_dotenv(override=True)


@click.group()
def cli() -> None:
    pass


cli.add_command(commands.ask)
cli.add_command(commands.categories)
cli.add_command(commands.run)
