import typer
from engine import FileEngine, TemplateEngine

app = typer.Typer(add_completion=False)

@app.command()
def analyze(template_path: str = typer.Argument(..., help="Path to the JSON template"),
            log_path: str = typer.Argument(..., help="Path to the Apache log file")):
    try:
        log_entries = FileEngine(log_path).run()
        template_analyzer = TemplateEngine(template_path).run()

        for entry in log_entries:
            response = template_analyzer(entry)
            if response is not None:
                typer.secho("[DETECTED]", fg=typer.colors.RED, bold=True)
                for key, value in response.items():
                    typer.secho(f"{key}: ", fg=typer.colors.YELLOW, bold=True, nl=False)
                    typer.echo(str(value))
                typer.echo()  # blank line between detections

    except Exception as e:
        typer.secho(f"[Error] {e}", fg=typer.colors.RED, err=True, bold=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
