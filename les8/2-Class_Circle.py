class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def calc_surface(self):
        from sympy import pi
        return self._radius ** 2 * pi

    def calc_circumference(self):
        from sympy import pi
        return self._radius * 2 * pi


# Feels dumb to make this a subclass. It's not a "variant" of a circle, it's more like an expansion.
# I could add a class Circle object as an argument, but I feel like that's just messy, since we can't give it its own
# radius then, only a Circle class object.
# EDIT: Instead of it being a subclass, I gave it the object "_ground_plane" (class Circle) as one of its variables.
# This means _radius isn't a variable in the class Cylinder, so we'll have to type:
# self._ground_plane.get_radius() instead of self._radius()
# We could fix this by adding another variable in the class itself, but if we change this, we also need to change
# the radius in the _ground_plane object.... This is damn messy in general.
# EDIT: Never thought about the get_radius() and set_radius() functions. I am a moron.
class Cylinder:
    def __init__(self, radius, height):
        self._ground_plane = Circle(radius)
        self._height = height

    def get_height(self):
        return self._height

    def get_radius(self):
        return self._ground_plane.get_radius()

    def set_height(self, height):
        self._height = height

    def set_radius(self, radius):
        self._ground_plane.set_radius(radius)

    def calc_surface(self):
        return self._ground_plane.calc_surface() * 2 + self._ground_plane.calc_circumference() * self._height

    def calc_volume(self):
        return self._ground_plane.calc_surface() * self._height


def main():
    circle = Circle(5)
    cylinder = Cylinder(5, 5)

    print(circle.calc_surface())
    print(circle.calc_circumference())

    print(cylinder.calc_surface())
    print(cylinder.calc_volume())


main()
