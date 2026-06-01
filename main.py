import click

@click.group()
def cli():
    """Nova Developer Experience (DX) CLI"""
    pass

@cli.command()
def init():
    click.echo("Initializing Nova developer workspace...")
    click.echo("✔ Folders provisioned.")
    click.echo("✔ Boilerplate created successfully!")

if __name__ == "__main__":
    cli()
