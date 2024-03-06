import click
import platform

@click.command()
def check_os():
    """Determines the operating system of the system."""
    os_name = platform.system()
    click.echo(f"The operating system is: {os_name}")

def register(cli):
    cli.add_command(check_os)

#if __name__ == "__main__":
#    check_os()
