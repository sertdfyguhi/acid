# standard d65
xn = 95.0489
yn = 100
zn = 108.8840


def f(t):
    return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116


class LabMixin:
    """Mixin to add CIELab conversion functions."""

    def to_lab(self) -> tuple[int | float]:
        """
        Converts the Colour object into Lab.

        Returns:
            tuple[int | float] consisting of:
        """

        # aint accurate bruh
        x, y, z = self.to_xyz()
        yt = f(y)

        return (
            (116 * yt - 16) / xn,
            (500 * (f(x) - yt)) / yn,
            (200 * (yt - f(z))) / zn,
        )

    @classmethod
    def from_lab(cls, h: int | float, s: int | float, l: int | float):
        """
        Creates a Colour object from a Lab colour.

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
