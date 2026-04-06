from __future__ import annotations
from dataclasses import dataclass
import random

from ..types import HexType
from .rgb import RGBA, RGB_INT, RGB_FLOAT
from .base_class import ColorContainer

@dataclass
class Hex(ColorContainer[HexType]):
    value: HexType

    def __post_init__(self):
        if self.value[0] != "#":
            raise ValueError("Hex color must start with #")
        if len(self.value) != 7:
            raise ValueError("Hex color must be 7 characters long")
        hex_str = self.value[1:]
        if len(hex_str) != 6:
            raise ValueError(f"Invalid HEX color: {self.value}")
        if not all(c.isdigit() or c.lower() in "abcdef" for c in hex_str):
            raise ValueError("Hex color must be a valid hex color")

    @classmethod
    def create_random(cls) -> Hex:
        """
        Create a random color container.

        Returns
        -------
        Hex: The random color container.
        """
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        hex_str = f"#{r:02x}{g:02x}{b:02x}"
        return cls(value=hex_str)

    @property
    def r(self) -> int:
        return int(self.value[1:3], 16)

    @property
    def g(self) -> int:
        return int(self.value[3:5], 16)

    @property
    def b(self) -> int:
        return int(self.value[5:7], 16)

    @classmethod
    def from_rgb_int(
        cls, 
        color: RGB_INT
        ) -> Hex:
        """
        Convert RGB_INT to Hex.

        Parameters
        ----------
        color: RGB_INT
            RGB_INT instance with value RgbInt (0-255)

        Returns
        -------
        Hex
            Hex instance
        """
        hex_str = f"#{color.r:02x}{color.g:02x}{color.b:02x}"
        return cls(value=hex_str)

    @classmethod
    def from_rgba(
        cls, 
        color: RGBA
        ) -> Hex:
        """
        Convert RGBA to Hex.

        Parameters
        ----------
        color: RGBA
            RGBA instance with value RgbaInt

        Returns
        -------
        Hex
            Hex instance
        """
        hex_str = f"#{color.r:02x}{color.g:02x}{color.b:02x}"
        return cls(value=hex_str)

    @classmethod
    def from_rgb_float(
        cls, 
        color: RGB_FLOAT
        ) -> Hex:
        """
        Convert RGB_FLOAT to Hex.

        Parameters
        ----------
        color: RGB_FLOAT
            RGB_FLOAT instance with value RgbFloat (0.0-1.0)

        Returns
        -------
        Hex
            Hex instance
        """
        r = round(color.r * 255)
        g = round(color.g * 255)
        b = round(color.b * 255)
        hex_str = f"#{r:02x}{g:02x}{b:02x}"
        return cls(value=hex_str)

    @classmethod
    def from_hex(
        cls, 
        color: Hex
        ) -> Hex:
        """
        Convert the color to Hex format.

        Parameters
        ----------
        color: Hex
            The color in Hex format.

        Returns
        -------
        Hex: The color in Hex format.
        """
        return cls(value=color.value)

    @property
    def to_rgb_int(self) -> RGB_INT:
        """
        Convert Hex to RGB_INT.

        Returns
        -------
        RGB_INT
            RGB_INT instance
        """
        return RGB_INT(value=(self.r, self.g, self.b))

    def to_rgba(
        self, 
        alpha: int = 255
        ) -> RGBA:
        """
        Convert Hex to RGBA.

        Parameters
        ----------
        alpha: int, optional
            Alpha value (0-255), default is 255

        Returns
        -------
        RGBA
            RGBA instance
        """
        return RGBA(value=(self.r, self.g, self.b, alpha))

    @property
    def to_rgb_float(self) -> RGB_FLOAT:
        """
        Convert Hex to RGB_FLOAT.

        Returns
        -------
        RGB_FLOAT
            RGB_FLOAT instance
        """
        return RGB_FLOAT(value=(self.r / 255.0, self.g / 255.0, self.b / 255.0))

    @property
    def to_hex(self) -> Hex:
        """
        Convert the color to Hex format.

        Returns
        -------
        Hex: The color in Hex format.
        """
        return self
