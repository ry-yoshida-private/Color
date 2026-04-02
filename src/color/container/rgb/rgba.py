from __future__ import annotations
from dataclasses import dataclass
import random

from .rgb import RGBContainer
from .rgb_int import RGB_INT
from .rgb_float import RGB_FLOAT
from ..hex import Hex


@dataclass
class RGBA(RGBContainer):
    value: tuple[int, int, int, int]

    def __post_init__(self):
        r, g, b, a = self.value
        for channel, name in zip((r, g, b), ('r', 'g', 'b')):
            if not (0 <= channel <= 255):
                raise ValueError(f"{name} must be between 0 and 255 (got {channel})")
        if not (0 <= a <= 255):
            raise ValueError(f"alpha must be between 0 and 255 (got {a})")

    @classmethod
    def create_random(cls) -> RGBA:
        """
        Create a random color container.

        Returns
        -------
        RGBA: The random color container.
        """
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        a = random.randint(0, 255)
        return cls(value=(r, g, b, a))

    @property
    def r(self) -> int:
        return self.value[0]

    @property
    def g(self) -> int:
        return self.value[1]

    @property
    def b(self) -> int:
        return self.value[2]

    @property
    def alpha(self) -> int:
        return self.value[3]

    @classmethod
    def from_rgb_int(
        cls,
        color: RGB_INT,
        alpha: int = 255
        ) -> RGBA:
        """
        Convert RGB_INT to RGBA.

        Parameters
        ----------
        color: RGB_INT
            RGB_INT instance with value tuple[int, int, int]
        alpha: int, optional
            Alpha value (0-255), default is 255

        Returns
        -------
        RGBA
            RGBA instance
        """
        return cls(value=(color.r, color.g, color.b, alpha))

    @classmethod
    def from_rgba(
        cls,
        color: RGBA
        ) -> RGBA:
        """
        Convert the color to RGBA format.

        Parameters
        ----------
        color: RGBA
            The color in RGBA format.

        Returns
        -------
        RGBA: The color in RGBA format.
        """
        return cls(value=color.value)

    @classmethod
    def from_rgb_float(
        cls,
        color: RGB_FLOAT,
        alpha: int = 255
        ) -> RGBA:
        """
        Convert RGB_FLOAT to RGBA.

        Parameters
        ----------
        color: RGB_FLOAT
            RGB_FLOAT instance with value tuple[float, float, float] (0.0-1.0)
        alpha: int, optional
            Alpha value (0-255), default is 255

        Returns
        -------
        RGBA
            RGBA instance
        """
        r = round(color.r * 255)
        g = round(color.g * 255)
        b = round(color.b * 255)
        return cls(value=(r, g, b, alpha))

    @classmethod
    def from_hex(
        cls,
        color: Hex,
        alpha: int = 255
        ) -> RGBA:
        """
        Convert Hex to RGBA.

        Parameters
        ----------
        color: Hex
            Hex instance with value str (e.g., "#ff0000")
        alpha: int, optional
            Alpha value (0-255), default is 255

        Returns
        -------
        RGBA
            RGBA instance
        """
        r, g, b = cls._parse_hex(color.value)
        return cls(value=(r, g, b, alpha))

    @property
    def to_rgb_int(self) -> RGB_INT:
        """
        Convert RGBA to RGB_INT.

        Returns
        -------
        RGB_INT
            RGB_INT instance
        """
        return RGB_INT(value=(self.r, self.g, self.b))

    @property
    def to_rgba(self) -> RGBA:
        """
        Convert the color to RGBA format.

        Returns
        -------
        RGBA: The color in RGBA format.
        """
        return self

    @property
    def to_rgb_float(self) -> RGB_FLOAT:
        """
        Convert RGBA to RGB_FLOAT.

        Returns
        -------
        RGB_FLOAT
            RGB_FLOAT instance
        """
        return RGB_FLOAT(value=(self.r / 255.0, self.g / 255.0, self.b / 255.0))

    @property
    def to_hex(self) -> Hex:
        """
        Convert RGBA to Hex.

        Returns
        -------
        Hex
            Hex instance
        """
        hex_str = self._format_hex(self.r, self.g, self.b)
        return Hex(value=hex_str)
