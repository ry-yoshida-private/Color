from __future__ import annotations
import colorsys
from dataclasses import dataclass
import random
from typing import TYPE_CHECKING

from ..types import HsvFloatType
from .base_class import ColorContainer
from .rgb.rgb_int import RGB_INT

if TYPE_CHECKING:
    from .hex import Hex
    from .rgb.rgb_float import RGB_FLOAT


@dataclass
class HSV(ColorContainer[HsvFloatType]):
    """
    HSV color with hue, saturation, and value in [0.0, 1.0] (same convention as colorsys).
    """

    value: HsvFloatType

    def __post_init__(self) -> None:
        if len(self.value) != 3:
            raise ValueError(f"HSV must have 3 channels (got {len(self.value)})")
        for ch_value in self.value:
            if not (0.0 <= float(ch_value) <= 1.0):
                raise ValueError(f"Value must be between 0.0 and 1.0 (got {self.value})")

    @classmethod
    def create_random(cls) -> HSV:
        """Create a random HSV color (uniform in h, s, v)."""
        h = random.random()
        s = random.random()
        v = random.random()
        return cls(value=(h, s, v))

    @property
    def h(self) -> float:
        return float(self.value[0])

    @property
    def s(self) -> float:
        return float(self.value[1])

    @property
    def v(self) -> float:
        return float(self.value[2])

    @classmethod
    def from_rgb_int(cls, color: RGB_INT) -> HSV:
        """Build HSV from sRGB integers (0–255)."""
        h, s, v = colorsys.rgb_to_hsv(color.r / 255.0, color.g / 255.0, color.b / 255.0)
        return cls(value=(h, s, v))

    @classmethod
    def from_rgb_float(cls, color: RGB_FLOAT) -> HSV:
        """Build HSV from linear RGB channels in [0.0, 1.0]."""
        h, s, v = colorsys.rgb_to_hsv(color.r, color.g, color.b)
        return cls(value=(h, s, v))

    @classmethod
    def from_hex(cls, color: Hex) -> HSV:
        """Build HSV from a hex color string."""
        return cls.from_rgb_int(RGB_INT.from_hex(color))

    @classmethod
    def from_hsv(cls, color: HSV) -> HSV:
        """Copy from another HSV container."""
        return cls(value=color.value)

    @property
    def to_rgb_int(self) -> RGB_INT:
        """Convert to RGB integers (0–255)."""
        r, g, b = colorsys.hsv_to_rgb(self.h, self.s, self.v)
        return RGB_INT(value=(round(r * 255), round(g * 255), round(b * 255)))

    @property
    def to_rgb_float(self) -> RGB_FLOAT:
        """Convert to RGB float channels in [0.0, 1.0]."""
        from .rgb.rgb_float import RGB_FLOAT

        r, g, b = colorsys.hsv_to_rgb(self.h, self.s, self.v)
        return RGB_FLOAT(value=(r, g, b))

    @property
    def to_hex(self) -> Hex:
        """Convert to #rrggbb hex."""
        return self.to_rgb_int.to_hex

    @property
    def to_hsv(self) -> HSV:
        return self
