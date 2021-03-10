import click


@click.command()
def version():
    """Display the current version."""
    click.echo(_read_version())