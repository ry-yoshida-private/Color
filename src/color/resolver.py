from __future__ import annotations

from typing import Any, cast

import numpy as np
from numpy.typing import NDArray

from .types import ColorFormat


class ColorFormatResolver:
    """Infer ColorFormat from raw values (internal use)."""

    @staticmethod
    def resolve(color: Any) -> ColorFormat:
        """
        Infer ColorFormat from a raw value.

        Parameters
        ----------
        color: Any
            Value to classify (str, length-3/4 tuple, or 1-D ndarray).

        Returns
        -------
        ColorFormat
            The inferred format. Three float channels are always RGB_FLOAT (same shape as
            HSV); use HSV constructors explicitly for hue/saturation/value tuples.

        Raises
        ------
        ValueError
            If color does not match any supported format.
        """
        match color:
            case str():
                color_format = ColorFormat.HEX
            case (int(), int(), int(), int()):
                color_format = ColorFormat.RGBA_INT
            case (int(), int(), int()):
                color_format = ColorFormat.RGB_INT
            case (float() | int(), float() | int(), float() | int()):
                color_format = ColorFormat.RGB_FLOAT
            case _ if isinstance(color, np.ndarray):
                color_format = ColorFormatResolver._infer_ndarray(cast(NDArray[Any], color))
            case _:
                raise ValueError(f"Invalid color value: {color!r}")
        return color_format

    @staticmethod
    def _infer_ndarray(color: NDArray[Any]) -> ColorFormat:
        if color.ndim != 1:
            raise ValueError(f"Color array must be 1D, got {color.ndim}D")

        n = color.shape[0]
        is_int = np.issubdtype(color.dtype, np.integer)
        is_float = np.issubdtype(color.dtype, np.floating)

        match (n, is_int, is_float):
            case (4, True, _):
                return ColorFormat.RGBA_INT
            case (3, True, _):
                return ColorFormat.RGB_INT
            case (3, _, True):
                return ColorFormat.RGB_FLOAT
            case _:
                raise ValueError(
                    f"Unsupported array shape or dtype: shape={color.shape}, dtype={color.dtype}"
                )
