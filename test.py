from acid import Colour

colour = Colour.from_rgb(100, 50, 25)
print(Colour.from_lab(*colour.to_lab()))
