from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .rgb.rgb_int import RGB_INT

class ColorContainer(ABC):
    """
    Base class for color containers.
    """
    @classmethod
    @abstractmethod
    def create_random(cls) -> ColorContainer:
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
    def from_rgb_int(
        cls, 
        color: RGB_INT
        ) -> ColorContainer:
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