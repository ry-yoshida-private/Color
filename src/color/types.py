from __future__ import annotations
import numpy as np
from enum import Enum
from types import UnionType


from typing import Any, TypeAlias, TYPE_CHECKING, TypeVar

from numpy.typing import NDArray

if TYPE_CHECKING:
    from .container import ColorContainer

RgbIntType: TypeAlias = tuple[int, int, int] | NDArray[np.integer]
RgbFloatType: TypeAlias = tuple[float, float, float] | NDArray[np.floating]
RgbaIntType: TypeAlias = tuple[int, int, int, int] | NDArray[np.integer]
HexType: TypeAlias = str
HsvFloatType: TypeAlias = tuple[float, float, float] | NDArray[np.floating]
ColorType: TypeAlias = (
    RgbIntType | RgbFloatType | RgbaIntType | HexType | HsvFloatType
)

ColorValueT = TypeVar("ColorValueT", bound=ColorType)


class ColorFormat(Enum):
    RGB_INT = "rgb_int"
    RGB_FLOAT = "rgb_float"
    RGBA_INT = "rgba_int"
    HEX = "hex"
    HSV = "hsv"

    @property
    def type(self) -> UnionType | type[str]:
        """
        Allowed value shapes: types.UnionType for RGB* / HSV (tuple | ndarray) or str for HEX.

        Note: HsvFloatType and RgbFloatType are the same structural type; only the
        container (HSV vs RGB_FLOAT) distinguishes interpretation.
        """
        match self:
            case ColorFormat.RGB_INT:
                return RgbIntType
            case ColorFormat.RGB_FLOAT:
                return RgbFloatType
            case ColorFormat.RGBA_INT:
                return RgbaIntType
            case ColorFormat.HEX:
                return HexType
            case ColorFormat.HSV:
                return HsvFloatType

    @property
    def container_class(self) -> type[ColorContainer[Any]]:
        """
        Get the container class for the color format.

        Returns
        -------
        type[ColorContainer[Any]]: The container class for the color format.
        """
        match self:
            case ColorFormat.RGB_INT:
                from .container import RGB_INT
                class_ = RGB_INT
            case ColorFormat.RGB_FLOAT:
                from .container import RGB_FLOAT
                class_ = RGB_FLOAT
            case ColorFormat.RGBA_INT:
                from .container import RGBA
                class_ = RGBA
            case ColorFormat.HEX:
                from .container import Hex
                class_ = Hex
            case ColorFormat.HSV:
                from .container import HSV
                class_ = HSV
        return class_

    @classmethod
    def from_color(cls, color: Any) -> ColorFormat:
        """
        Build a ColorFormat from a raw color value.

        Parameters
        ----------
        color: Any
            Value to classify (str, length-3/4 tuple, or 1-D ndarray).

        Returns
        -------
        ColorFormat
            The inferred format. Length-3 float tuples and float ndarrays are treated as
            RGB_FLOAT, not HSV (indistinguishable at runtime). Build HSV via
            ColorFormat.HSV.container_class(value=...) or HSV.from_rgb_int / etc.

        Raises
        ------
        ValueError
            If color does not match any supported format.
        """
        from .resolver import ColorFormatResolver

        return ColorFormatResolver.resolve(color)