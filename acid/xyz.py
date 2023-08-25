class XYZMixin:
    """Mixin to add CIEXYZ conversion functions."""

    def to_xyz(self) -> tuple[int | float]:
        """
        Converts the Colour object into XYZ. Assumes Colour object is in the sRGB colour space.

        Returns:
            tuple[int | float (0.0 - 1.0)] consisting of normalized XYZ values
        """
        # linearize sRGB data
        rgb = (self.r / 255, self.g / 255, self.b / 255)
        rt, gt, bt = (
            c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb
        )

        # transformation matrix
        return (
            0.4124564 * rt + 0.3575761 * gt + 0.1804375 * bt,
            0.2126729 * rt + 0.7151522 * gt + 0.0721750 * bt,
            0.0193339 * rt + 0.1191920 * gt + 0.9503041 * bt,
        )

    @classmethod
    def from_xyz(cls, x: int | float, y: int | float, z: int | float):
        """
        Creates a Colour object from a XYZ colour.

        Args:
            x: int | float (0.0 - 1.0)
                Normalized X value.
            y: int | float (0.0 - 1.0)
                Normalized Y value.
            z: int | float (0.0 - 1.0)
                Normalized Z value.

        Returns: Colour
        """
        # transformation matrix
        rgbt = (
            3.2404542 * x + -1.5371385 * y + -0.4985314 * z,
            -0.9692660 * x + 1.8760108 * y + 0.0415560 * z,
            0.0556434 * x + -0.2040259 * y + 1.0572252 * z,
        )

        # apply gamma
        r, g, b = (
            c * 12.92 if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
            for c in rgbt
        )

        return cls(r * 255, g * 255, b * 255)
