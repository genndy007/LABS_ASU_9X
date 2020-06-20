from math import pi
class Circle:
    def __init__(self, r):    # Constructor
        self.__r = r

    def get_radius(self):   # getting radius from private attribute
        return self.__r

    def figure_volume(self):    # Defining abstract method
        pass

class Cone(Circle):
    def __init__(self, r, h):    # Constructor
        super().__init__(r)
        self.h = h

    def figure_volume(self):    # Redefining it in child class
        volume = (1/3)*pi*(self.get_radius())**2*self.h
        return volume


print("Written in Python 3,\nAssignment completed by Kochev Hennadii, IP-91,\nip9113, variant (13+91)%27+1 = 24\n")

radius = 3
height = 5

cone = Cone(radius, height)
vol = cone.figure_volume()

print(f"Volume of cone with r={radius}, h={height}:", vol)



