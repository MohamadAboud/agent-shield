# """ Third-party modules """
import click

@click.command()
@click.argument("question", type=str, required=True)
def ask(question: str) -> None:
    """
    Ask the GuardianAI a question.
    """
    click.echo("Running the GuardianAI...")
    from .guardian_ai import GuardianAI
    # Initialize the GuardianAI
    guardian = GuardianAI()
    # print("Running the GuardianAI...")
    res = guardian.invoke(question)
    click.echo(click.style(res, fg="green"))


@click.command()
@click.argument("name", type=str, required=False)
@click.argument("id", type=int, required=False)
def categories(name: str, id: int) -> None:
    """
    Get the GuardianAI categories.
    """
    from .guardian_ai.guardian_category import GuardianCategory
    # print("Getting the GuardianAI categories...")
    categorie = GuardianCategory.from_type(name or id)
    click.echo("\n"+str(categorie)+"\n")


@click.group()
def run() -> None:
    """
    Run the GuardianAI.
    """
    pass



# Add run api
@run.command()
@click.option("--host", type=str, default="0.0.0.0", help="The host of the API.")
@click.option("--port", type=int, default=7651, help="The port of the API.")
@click.option("--debug", type=bool, default=False, help="The debug mode of the API.")
def api(host: str, port: int, debug: bool) -> None:
    """
    Run the GuardianAI API.
    """
    click.echo("Running the GuardianAI API...")
    from .api.api import run as run_api_server  
    run_api_server(host, port, debug)
    


# Add run ui
@run.command()
@click.option("--host", type=str, default="0.0.0.0", help="The host of the API.")
@click.option("--port", type=int, default=7652, help="The port of the API.")
def ui(host: str, port: int) -> None:
    """
    Run the GuardianAI UI.
    """
    click.echo("Running the GuardianAI UI...")
    from .ui.ui import run as run_ui_server
    run_ui_server(host, port)
