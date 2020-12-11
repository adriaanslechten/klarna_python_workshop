"""
Class containing the item. THis is used inside of the Gilded Rose code kata.
"""
from dataclasses import dataclass


@dataclass
class Item:
    """Class for item"""

    name: str
    sell_in: int
    quality: int
