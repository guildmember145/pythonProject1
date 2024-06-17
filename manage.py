#usr/bin/env python


import typer
import uvicorn


manager = typer.Typer()

@manager.command()
def run_server(reload: bool = True):
    uvicorn.run(
        "main:app",
          host="0.0.0.0",
            port=5000,
            reload=reload,
            )
    

    typer.echo("Server is running")


if __name__ == "__main__":
    manager()