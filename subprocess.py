import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()


@app.command("list")
def sample_func():
    subprocess.run(f"ls -l", shell=True)

@app.command("hello")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yello]")



if __name__ == "__main__":
    app()