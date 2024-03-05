import click

def register(cli):
    @cli.command()
    def hello_world():
        """Say hello."""
        click.echo("Hello World!")
#    click.echo("Hello, World!")
