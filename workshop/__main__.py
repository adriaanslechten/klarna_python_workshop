import click
from click import group

from workshop.items.items import Item


@group()
def main() -> None:
    """This is the Gilded rose CLI"""
    click.echo("Running the CLI")


@main.command()
@click.option(
    "--replicate", type=int, help="Replicate X copies of item", default=4
)
@click.option("--name", type=str, help="Name of the Item", default="Aged brie")
@click.option("--sell-in", type=int, help="Sell-in of the item", default="10")
@click.option("--quality", type=int, help="Quality of the item", default="20")
def replicate_item(replicate, name, sell_in, quality):
    """Create x replicates of a item"""
    items = [Item(name, sell_in, quality) for item in range(replicate) ]
    print(f"The number of items replicated is: {len(items)}.")
    return items
