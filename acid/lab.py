from .xyz import xn, yn, zn
import math

# constants
d = 6 / 29
d1 = d**3
d2 = 2 * d**2

p = 4 / 29


def f(t):
    return math.cbrt(t) if t > d1 else t / d2 + p


def inv_f(t):
    return t**3 if t > d else d2 * (t - p)


class LabMixin:
    """Mixin to add CIELAB conversion functions."""

    def to_lab(self, normalize: bool = True) -> tuple[int | float]:
        """
        Converts the Colour object into Lab.

        Args:
            normalize: bool = True
                If true, normalizes the Lab values before returning.

        Returns:
            tuple[int | float] consisting of:
        """
        x, y, z = self.to_xyz()
        yt = f(y)
        L = 116 * yt - 16
        a = 500 * (f(x) - yt)
        b = 200 * (yt - f(z))

        if normalize:
            return (L / xn, a / yn, b / zn)
        else:
            return (L, a, b)

    @classmethod
    def from_lab(cls, l: int | float, a: int | float, b: int | float):
        """
        Creates a Colour object from a Lab colour.

        Args:
            l: int | float (0.0 - 1.0)
                Normalized L value.
            a: int | float (0.0 - 1.0)
                Normalized a value.
            b: int | float (0.0 - 1.0)
                Normalized b valie.

        Returns: Colour
        """
        lp = (l + 16) / 116
        x = xn * inv_f(lp + a / 500)
        y = yn * inv_f(lp)
        z = zn * inv_f(lp - b / 200)

        return cls.from_xyz(x, y, z)
