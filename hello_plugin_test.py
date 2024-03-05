import click

def register(cli):
    @cli.command()
    def hello_test():
        """Say hello."""
        click.echo("Hello from the GH plugin!")
