"""Console script for spectrum."""
import sys
import click

import click

from .genotype import commands as genotype
from .cna import commands as cna

@click.group()
def entry_point():
    pass

entry_point.add_command(genotype.command_group)
entry_point.add_command(cna.version)

@click.command()
def main(args=None):
    """Console script for spectrum."""
    click.echo("Replace this message by putting your code into "
               "spectrum.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
