import numpy as np
from dataclasses import dataclass, field

from .color_converter import ColorConverter
from .types import HexType, RgbIntType

@dataclass
class ID2IntColor:
    """
    A class for managing colors for unique identifiers.

    Attributes
    ----------
    color_dict: dict[str, RgbInt]
        A dictionary to store the assigned colors in RGB format for each ID.
    """
    color_dict: dict[str, RgbIntType] = field(default_factory=dict)

    def get_rgb_int_color(
        self, 
        id_: str, 
        ) -> RgbIntType:
        """
        Get the RGB color associated with the given ID.

        Parameters:
        ----------
        id_: str
            The unique identifier for which to get the color.

        Returns:
        ----------
        RgbInt
            The RGB color associated with the given ID.
        """
        rgb_int_color = self._attribute_color_dict(id_)
        return rgb_int_color

    def get_bgr_int_color(
        self, 
        id_: str, 
        ) -> RgbIntType:
        """
        Get the BGR color associated with the given ID.

        Parameters:
        ----------
        id_: str
            The unique identifier for which to get the BGR color.

        Returns:
        ----------
        RgbInt
            The BGR color associated with the given ID.
        """
        rgb_int_color = self._attribute_color_dict(id_=id_)
        return ColorConverter.RGB_INT2BGR_INT(color=rgb_int_color)

    def get_hex_color(
        self, 
        id_: str,
        ) -> HexType:
        """
        Get the hex color associated with the given ID.

        Parameters:
        ----------
        id_: str
            The unique identifier for which to get the hex color.

        Returns:
        ----------
        HexColor
            The hex color associated with the given ID.
        """
        rgb_int_color = self._attribute_color_dict(id_=id_)
        return ColorConverter.RGB_INT2HEX(color=rgb_int_color)

    def _attribute_color_dict(self, id_: str) -> RgbIntType:
        """
        Attribute a RGB color to the given ID.
        
        Parameters:
        ----------
        id_: str
            The unique identifier for which to attribute a color.

        Returns:
            RgbInt
            The RGB color associated with the given ID.
        """

        rgb_int_color = self.color_dict.get(id_, None)

        if rgb_int_color is None:
            # Generate a new random RGB color
            t = np.random.randint(0, 256, 3).tolist()
            rgb_int_color = (int(t[0]), int(t[1]), int(t[2]))
            self.color_dict[id_] = rgb_int_color
        return rgb_int_color
    
    def __str__(self):
        return f"ID2IntColor(color_dict={self.color_dict})"

    def __repr__(self):
        return self.__str__()

