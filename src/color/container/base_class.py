from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Callable, Generic, TypeVar, cast

from ..types import ColorType, ColorValueT

if TYPE_CHECKING:
    from .rgb.rgb_int import RGB_INT

ContainerT = TypeVar("ContainerT", bound="ColorContainer[Any]")


class ColorContainer(Generic[ColorValueT], ABC):
    """
    Base class for color containers.
    """

    value: ColorValueT

    @classmethod
    @abstractmethod
    def create_random(cls: type[ContainerT]) -> ContainerT:
        """
        Create a random color container.
        """

    @property
    @abstractmethod
    def to_rgb_int(self) -> RGB_INT:
        """
        Convert the color to RGB integer format.

        Returns
        -------
        RGB_INT: The color in RGB integer format.
        """

    @classmethod
    @abstractmethod
    def from_rgb_int(cls: type[ContainerT], color: RGB_INT) -> ContainerT:
        """
        Convert the color to RGB integer format.

        Parameters
        ----------
        color: RGB_INT
            The color in RGB integer format.

        Returns
        -------
        ColorContainer: The color container.
        """

    @classmethod
    def register(cls, color: ColorType) -> ColorContainer[Any]:
        from ..types import ColorFormat

        color_format = ColorFormat.from_color(color)
        color_class = color_format.container_class
        factory = cast(Callable[..., ColorContainer[Any]], color_class)
        return factory(value=color)

