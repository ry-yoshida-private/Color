from __future__ import annotations
from abc import ABC

from ..base_class import ColorContainer

class RGBContainer(ColorContainer, ABC):
    """
    Base class for RGB series color containers (RGB_INT, RGBA, RGB_FLOAT).
    """

    @staticmethod
    def _parse_hex(hex_str: str) -> tuple[int, int, int]:
        """
        Parse hex color string to (r, g, b) integers.

        Parameters
        ----------
        hex_str : str
            Hex string without '#' (e.g. "ff0000")

        Returns
        -------
        tuple[int, int, int]
            (r, g, b) in 0-255
        """
        hex_str = hex_str.lstrip("#")
        if len(hex_str) != 6:
            raise ValueError(f"Invalid HEX color length: {hex_str}")
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)
        return (r, g, b)

    @staticmethod
    def _format_hex(
        r: int, 
        g: int, 
        b: int
        ) -> str:
        """
        Format (r, g, b) integers to hex color string.

        Parameters
        ----------
        r, g, b : int
            Channel values in 0-255

        Returns
        -------
        str
            Hex string (e.g. "#ff0000")
        """
        return f"#{r:02x}{g:02x}{b:02x}"
