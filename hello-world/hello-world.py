import click

@click.command()
def hello_world():
    """A simple plugin that prints 'Hello, World!'"""
    click.echo("Hello, World!")
