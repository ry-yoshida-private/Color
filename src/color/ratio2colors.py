from .color_converter import ColorConverter
from .types import RgbIntType


class Ratio2IntColor:
    def __init__(self):
        self.colors: list[RgbIntType] = [
            (139, 0, 0),    # 0.0 - 0.1  dark red (RGB)
            (178, 34, 34),  # 0.1 - 0.2  firebrick (RGB)
            (255, 69, 0),   # 0.2 - 0.3  orange red (RGB)
            (255, 140, 0),  # 0.3 - 0.4  dark orange (RGB)
            (255, 165, 0),  # 0.4 - 0.5  orange (RGB)
            (255, 215, 0),  # 0.5 - 0.6  gold (RGB)
            (173, 255, 47), # 0.6 - 0.7  green yellow (RGB)
            (127, 255, 0),  # 0.7 - 0.8  chartreuse (RGB)
            (50, 205, 50),  # 0.8 - 0.9  lime green (RGB)
            (0, 206, 209),  # 0.9 - 1.0  dark turquoise (RGB)
        ]
        
    def get_rgb_int_color(
        self,
        ratio: float
        ) -> RgbIntType:
        """
        Get the RGB color associated with the given ratio.

        Parameters:
        ----------
        ratio: float
            The ratio value to get the color for.

        Returns:
        ----------
        RgbInt
            The RGB color associated with the given ratio.
        """
        index = min(int(ratio * 10), 9)  # clamp to 0–9
        rgb_int_color = self.colors[index]
        return rgb_int_color
        
    def get_bgr_int_color(
        self, 
        ratio: float,
        ) -> RgbIntType:
        """
        Get the BGR color associated with the given ratio.

        Parameters:
        ----------
        ratio: float
            The ratio value to get the color for.

        Returns:
        ----------
        RgbInt
            The BGR color associated with the given ratio.
        """
        rgb_int_color = self.get_rgb_int_color(ratio=ratio)
        return ColorConverter.RGB_INT2BGR_INT(color=rgb_int_color)

    def __str__(self) -> str:
        return f"Ratio2IntColor(colors={self.colors})"

    def __repr__(self) -> str:
        return self.__str__()
