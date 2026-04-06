from __future__ import annotations
from dataclasses import dataclass
import random
from typing import TYPE_CHECKING

from ...types import RgbFloatType
from .rgb import RGB
from .rgb_int import RGB_INT

if TYPE_CHECKING:
    from ..hex import Hex
    from .rgba import RGBA


@dataclass
class RGB_FLOAT(RGB[RgbFloatType]):
    value: RgbFloatType

    def __post_init__(self):
        if len(self.value) != 3:
            raise ValueError(f"RGB_FLOAT must have 3 channels (got {len(self.value)})")
        for ch_value in self.value:
            if not (0.0 <= ch_value <= 1.0):
                raise ValueError(f"Value must be between 0.0 and 1.0 (got {self.value})")

    @classmethod
    def create_random(cls) -> RGB_FLOAT:
        """
        Create a random color container.

        Returns
        -------
        RGB_FLOAT: The random color container.
        """
        r = random.random()
        g = random.random()
        b = random.random()
        return cls(value=(r, g, b))

    @property
    def r(self) -> float:
        return self.value[0]

    @property
    def g(self) -> float:
        return self.value[1]

    @property
    def b(self) -> float:
        return self.value[2]

    @classmethod
    def from_rgb_int(
        cls,
        color: RGB_INT
        ) -> RGB_FLOAT:
        """
        Convert RGB_INT to RGB_FLOAT.

        Parameters
        ----------
        color: RGB_INT
            RGB_INT instance with value RgbInt (0-255)

        Returns
        -------
        RGB_FLOAT
            RGB_FLOAT instance
        """
        return cls(value=(color.r / 255.0, color.g / 255.0, color.b / 255.0))

    @classmethod
    def from_rgba(
        cls,
        color: RGBA
        ) -> RGB_FLOAT:
        """
        Convert RGBA to RGB_FLOAT.

        Parameters
        ----------
        color: RGBA
            RGBA instance with value RgbaInt

        Returns
        -------
        RGB_FLOAT
            RGB_FLOAT instance
        """
        return cls(value=(color.r / 255.0, color.g / 255.0, color.b / 255.0))

    @classmethod
    def from_rgb_float(
        cls,
        color: RGB_FLOAT
        ) -> RGB_FLOAT:
        """
        Convert the color to RGB float format.

        Parameters
        ----------
        color: RGB_FLOAT
            The color in RGB float format.

        Returns
        -------
        RGB_FLOAT: The color in RGB float format.
        """
        return cls(value=color.value)

    @classmethod
    def from_hex(
        cls,
        color: Hex
        ) -> RGB_FLOAT:
        """
        Convert Hex to RGB_FLOAT.

        Parameters
        ----------
        color: Hex
            Hex instance with value str (e.g., "#ff0000")

        Returns
        -------
        RGB_FLOAT
            RGB_FLOAT instance
        """
        r, g, b = cls._parse_hex(color.value)
        return cls(value=(r / 255.0, g / 255.0, b / 255.0))

    @property
    def to_rgb_int(self) -> RGB_INT:
        """
        Convert RGB_FLOAT to RGB_INT.

        Returns
        -------
        RGB_INT
            RGB_INT instance
        """
        return RGB_INT(value=(round(self.r * 255), round(self.g * 255), round(self.b * 255)))

    def to_rgba(
        self,
        alpha: int = 255
        ) -> RGBA:
        """
        Convert RGB_FLOAT to RGBA.

        Parameters
        ----------
        alpha: int, optional
            Alpha value (0-255), default is 255

        Returns
        -------
        RGBA
            RGBA instance
        """
        from .rgba import RGBA

        r = round(self.r * 255)
        g = round(self.g * 255)
        b = round(self.b * 255)
        return RGBA(value=(r, g, b, alpha))

    @property
    def to_rgb_float(self) -> RGB_FLOAT:
        """
        Convert the color to RGB float format.

        Returns
        -------
        RGB_FLOAT: The color in RGB float format.
        """
        return self

    @property
    def to_hex(self) -> Hex:
        """
        Convert RGB_FLOAT to Hex.

        Returns
        -------
        Hex
            Hex instance
        """
        from ..hex import Hex

        r = round(self.r * 255)
        g = round(self.g * 255)
        b = round(self.b * 255)
        hex_str = self._format_hex(r, g, b)
        return Hex(value=hex_str)
