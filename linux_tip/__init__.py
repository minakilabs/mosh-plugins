import click
import random

# List of Linux tips
TIPS = [
    "Use `grep` to search inside files. Example: `grep 'search_term' file.txt`",
    "Use `ctrl + r` to search through your previous commands.",
    "Use `cat file | grep something` to search for 'something' in the output of 'file'.",
    "Use `wget` to download files from the internet. Example: `wget http://example.com/file`",
    "Use `man <command>` to get the manual page of a command. For example, `man grep`.",
    # Add more tips as desired
]

@click.command()
def linux_tip():
    """Display a random Linux tip."""
    click.echo(random.choice(TIPS))

def register(cli):
    cli.add_command(linux_tip)
