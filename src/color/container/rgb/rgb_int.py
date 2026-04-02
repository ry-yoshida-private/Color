from __future__ import annotations
from dataclasses import dataclass
import random

from .rgb import RGBContainer
from .rgba import RGBA
from .rgb_float import RGB_FLOAT
from ..hex import Hex


@dataclass
class RGB_INT(RGBContainer):
    value: tuple[int, int, int]

    def __post_init__(self):
        r, g, b = self.value
        for channel, name in zip((r, g, b), ("r", "g", "b")):
            if not (0 <= channel <= 255):
                raise ValueError(f"{name} must be between 0 and 255 (got {channel})")

    @classmethod
    def create_random(cls) -> RGB_INT:
        """Create a random color container. Returns RGB_INT."""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return cls(value=(r, g, b))

    @property
    def r(self) -> int:
        return self.value[0]

    @property
    def g(self) -> int:
        return self.value[1]

    @property
    def b(self) -> int:
        return self.value[2]

    @classmethod
    def from_rgb_int(cls, color: RGB_INT) -> RGB_INT:
        """Convert the color to RGB integer format."""
        return cls(value=color.value)

    @classmethod
    def from_rgba(cls, color: RGBA) -> RGB_INT:
        """Convert RGBA to RGB_INT."""
        r, g, b, _ = color.value
        return cls(value=(r, g, b))

    @classmethod
    def from_rgb_float(cls, color: RGB_FLOAT) -> RGB_INT:
        """Convert RGB_FLOAT to RGB_INT."""
        r, g, b = color.value
        return cls(value=(round(r * 255), round(g * 255), round(b * 255)))

    @classmethod
    def from_hex(cls, color: Hex) -> RGB_INT:
        """Convert Hex to RGB_INT."""
        r, g, b = cls._parse_hex(color.value)
        return cls(value=(r, g, b))

    @property
    def to_rgb_int(self) -> RGB_INT:
        """Convert the color to RGB integer format."""
        return self

    def to_rgba(self, alpha: int = 255) -> RGBA:
        """Convert RGB_INT to RGBA."""
        return RGBA(value=(self.r, self.g, self.b, alpha))

    @property
    def to_rgb_float(self) -> RGB_FLOAT:
        """Convert RGB_INT to RGB_FLOAT."""
        return RGB_FLOAT(value=(self.r / 255.0, self.g / 255.0, self.b / 255.0))

    @property
    def to_hex(self) -> Hex:
        """Convert RGB_INT to Hex."""
        hex_str = self._format_hex(self.r, self.g, self.b)
        return Hex(value=hex_str)
