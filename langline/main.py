import os

import typer
from typing import List
from pipeline import pipeline

app = typer.Typer(add_completion=False)


@app.command()
def input(lang: List[str], audioname="input.mp3"):
    if len(lang) == 0:
        raise typer.BadParameter("No languages detected")
    else:
        try:
            pipeline("../../external/input/", audioname, lang)
        except Exception as e:
            typer.echo(f'{e} thrown from pipeline', err=True)
            raise typer.Exit(1)

def main():
    app()


if __name__ == "__main__":
    main()
