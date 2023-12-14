import os

import typer
from typing import List
from scripts import pipeline_class
from config import root_dir
app = typer.Typer(add_completion=False)

input_dir = f"{root_dir}/input/"
@app.command()
def input(lang: List[str], audioname):
    if len(lang) == 0:
        raise typer.BadParameter("No languages detected")
    else:
        try:
            pipeline_class.multi_process(input_dir, audioname, lang)
        except Exception as e:
            typer.echo(f'{e} thrown from pipeline', err=True)
            raise typer.Exit(1)

def main():
    app()


if __name__ == "__main__":
    main()
