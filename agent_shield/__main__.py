# """ Third-party modules """
import click
from dotenv import load_dotenv

# """ Local modules """
from agent_shield import commands


# Load the environment variables from the .env file
load_dotenv(override=True)


@click.group()
def cli() -> None:
    pass


cli.add_command(commands.ask)
cli.add_command(commands.categories)
cli.add_command(commands.run)

if __name__ == "__main__":
    cli()