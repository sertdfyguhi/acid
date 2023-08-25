class CMYKMixin:
    """Mixin to add CMYK conversion functions."""

    def to_cmyk(self) -> tuple[int | float]:
        """
        Converts the Colour object into a CMYK colour.

        Returns:
            tuple[int | float] consisting of:
                hue: in degrees
                saturation: as decimal percentage
                luminance: as decimal percentage
        """
        ...

    @classmethod
    def from_cmyk(cls, h: int | float, s: int | float, l: int | float):
        """
        Creates a Colour object from a CMYK colour.

        Args:
            h: int | float
                Hue in degrees.
            s: int | float
                Saturation as a decimal percentage (0.0 - 1.0).
            l: int | float
                Luminance as a decimal percentage (0.0 - 1.0).

        Returns: Colour
        """
        ...
