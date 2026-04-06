from .types import HexType, RgbFloatType, RgbIntType

class ColorConverter:
    """
    A utility class for converting colors between different formats.
    Supports RGB_INT, RGB_FLOAT, BGR_INT, BGR_FLOAT, GRAY_INT, GRAY_FLOAT, and HEX formats.
    """
    @staticmethod
    def RGB_INT2RGB_FLOAT(color: RgbIntType) -> RgbFloatType:
        """
        Convert RGB integer color to RGB float color.

        Parameters
        ----------
        color: RgbIntType
            The RGB integer color as (r, g, b) with values in 0-255.

        Returns
        -------
        RgbFloatType
            The RGB float color as (r, g, b) with values in 0.0-1.0.
        """
        r, g, b = color
        return (r / 255.0, g / 255.0, b / 255.0)

    @staticmethod
    def RGB_INT2BGR_INT(color: RgbIntType) -> RgbIntType:
        """
        Convert RGB integer color to BGR integer color.

        Parameters
        ----------
        color: RgbIntType
            The RGB integer color.

        Returns
        -------
        RgbIntType
            The BGR integer color (channels (b, g, r)).
        """
        r, g, b = color
        return (b, g, r)

    @staticmethod
    def RGB_INT2BGR_FLOAT(color: RgbIntType) -> RgbFloatType:
        """
        Convert RGB integer color to BGR float color.

        Parameters
        ----------
        color: RgbIntType
            The RGB integer color.

        Returns
        -------
        RgbFloatType
            The BGR float color (channels (b, g, r) in 0.0-1.0).
        """
        r, g, b = color
        return (b / 255.0, g / 255.0, r / 255.0)

    @staticmethod
    def RGB_INT2GRAY_INT(color: RgbIntType) -> int:
        """
        Convert RGB integer color to grayscale integer color.

        Parameters
        ----------
        color: RgbIntType
            The RGB integer color.

        Returns
        -------
        int
            The grayscale integer color (0-255).
        """
        r, g, b = color
        return int(0.299 * r + 0.587 * g + 0.114 * b)

    @staticmethod
    def RGB_INT2GRAY_FLOAT(color: RgbIntType) -> float:
        """
        Convert RGB integer color to grayscale float color.

        Parameters
        ----------
        color: RgbIntType
            The RGB integer color.

        Returns
        -------
        float
            The grayscale float color (0.0-1.0).
        """
        r, g, b = color
        return (0.299 * r + 0.587 * g + 0.114 * b) / 255.0

    @staticmethod
    def RGB_INT2HEX(color: RgbIntType) -> HexType:
        """
        Convert RGB integer color to HEX color string.

        Parameters
        ----------
        color: RgbIntType
            The RGB integer color.

        Returns
        -------
        HexType
            The HEX color string (e.g., "#ff0000").
        """
        r, g, b = color
        return f"#{r:02x}{g:02x}{b:02x}"

    @staticmethod
    def RGB_FLOAT2RGB_INT(color: RgbFloatType) -> RgbIntType:
        """
        Convert RGB float color to RGB integer color.

        Parameters
        ----------
        color: RgbFloatType
            The RGB float color.

        Returns
        -------
        RgbIntType
            The RGB integer color.
        """
        r, g, b = color
        return (round(r * 255), round(g * 255), round(b * 255))

    @staticmethod
    def BGR_INT2RGB_INT(color: RgbIntType) -> RgbIntType:
        """
        Convert BGR integer color to RGB integer color.

        Parameters
        ----------
        color: RgbIntType
            The BGR integer color (channels (b, g, r)).

        Returns
        -------
        RgbIntType
            The RGB integer color.
        """
        b, g, r = color
        return (r, g, b)

    @staticmethod
    def BGR_FLOAT2RGB_INT(color: RgbFloatType) -> RgbIntType:
        """
        Convert BGR float color to RGB integer color.

        Parameters
        ----------
        color: RgbFloatType
            The BGR float color (channels (b, g, r) in 0.0-1.0).

        Returns
        -------
        RgbIntType
            The RGB integer color.
        """
        b, g, r = color
        return (round(r * 255), round(g * 255), round(b * 255))

    @staticmethod
    def GRAY_INT2RGB_INT(color: int) -> RgbIntType:
        """
        Convert grayscale integer color to RGB integer color.

        Parameters
        ----------
        color: int
            The grayscale integer color (0-255).

        Returns
        -------
        RgbIntType
            The RGB integer color.
        """
        return (color, color, color)

    @staticmethod
    def GRAY_FLOAT2RGB_INT(color: float) -> RgbIntType:
        """
        Convert grayscale float color to RGB integer color.

        Parameters
        ----------
        color: float
            The grayscale float color (0.0-1.0).

        Returns
        -------
        RgbIntType
            The RGB integer color.
        """
        return (round(color * 255), round(color * 255), round(color * 255))

    @staticmethod
    def HEX2RGB_INT(color: HexType) -> RgbIntType:
        """
        Convert HEX color string to RGB integer color.

        Parameters
        ----------
        color: HexType
            The HEX color string (e.g., "#ff0000" or "ff0000").

        Returns
        -------
        RgbIntType
            The RGB integer color.

        Raises
        ------
        ValueError:
            If the HEX color string is invalid (not 6 hexadecimal characters).
        """
        hex_color = color.lstrip('#')
        if len(hex_color) != 6:
            raise ValueError(f"Invalid HEX color: {color}")
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return (r, g, b)
