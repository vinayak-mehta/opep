# -*- coding: utf-8 -*-

import os
import glob
import random
from io import StringIO

import click
from rich.console import Console
from rich.markdown import Markdown


def validate_number(ctx, param, value):
    try:
        _ = int(value)
        return value
    except ValueError:
        if value == "random":
            return value
        else:
            raise click.BadParameter("Argument should be an integer or 'random'")


@click.command("opep")
@click.argument("number", callback=validate_number)
@click.pass_context
def cli(*args, **kwargs):
    """Open PEPs on your terminal."""
    number = kwargs["number"]

    cwd = os.path.dirname(__file__)
    if number == "random":
        pep_path = random.choice(glob.glob(os.path.join(cwd, "peps/*.md")))
    else:
        pep_path = os.path.join(cwd, f"peps/pep-{number.zfill(4)}.md")

    with open(pep_path, "r") as f:
        pep_content = f.read()

    # https://github.com/willmcgugan/rich/issues/77#issuecomment-670659857
    console = Console(file=StringIO(), force_terminal=True)

    md = Markdown(pep_content)
    console.print(md)

    click.echo_via_pager(console.file.getvalue())
