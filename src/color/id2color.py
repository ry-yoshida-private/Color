import numpy as np
from dataclasses import dataclass, field
from .color_converter import ColorConverter

@dataclass
class ID2Color:
    """
    A class for managing colors for unique identifiers.

    Attributes
    ----------
    color_dict: dict[str, tuple[int, int, int]]
        A dictionary to store the assigned colors in RGB format for each ID.
    """
    color_dict: dict[str, tuple[int, int, int]] = field(default_factory=dict)

    def get_rgb_int_color(
        self, 
        id_: str, 
        ) -> tuple[int, int, int]:
        """
        Get the RGB color associated with the given ID.

        Parameters:
        ----------
        id_: str
            The unique identifier for which to get the color.

        Returns:
        ----------
        tuple[int, int, int]
            The RGB color associated with the given ID.
        """
        rgb_int_color = self._attribute_color_dict(id_)
        return rgb_int_color

    def get_bgr_int_color(
        self, 
        id_: str, 
        ) -> tuple[int, int, int]:
        """
        Get the BGR color associated with the given ID.

        Parameters:
        ----------
        id_: str
            The unique identifier for which to get the BGR color.

        Returns:
        ----------
        tuple[int, int, int]
            The BGR color associated with the given ID.
        """
        rgb_int_color = self._attribute_color_dict(id_=id_)
        return ColorConverter.RGB_INT2BGR_INT(color=rgb_int_color)

    def get_hex_color(
        self, 
        id_: str,
        ) -> str:
        """
        Get the hex color associated with the given ID.

        Parameters:
        ----------
        id_: str
            The unique identifier for which to get the hex color.

        Returns:
        ----------
        hex_color: str
            The hex color associated with the given ID.
        """
        rgb_int_color = self._attribute_color_dict(id_=id_)
        return ColorConverter.RGB_INT2HEX(color=rgb_int_color)

    def _attribute_color_dict(self, id_: str) -> tuple[int, int, int]:
        """
        Attribute a RGB color to the given ID.
        
        Parameters:
        ----------
        id_: str
            The unique identifier for which to attribute a color.

        Returns:
            tuple[int, int, int]
            The RGB color associated with the given ID.
        """

        rgb_int_color = self.color_dict.get(id_, None)

        if rgb_int_color is None:
            # Generate a new random RGB color
            rgb_int_color = tuple(np.random.randint(0, 256, 3).tolist())
            self.color_dict[id_] = rgb_int_color
        return rgb_int_color
    
    def __str__(self):
        return f"ID2Color(color_dict={self.color_dict})"

    def __repr__(self):
        return self.__str__()

