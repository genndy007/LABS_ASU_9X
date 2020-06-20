from math import pi
class Figure:   # Abstract class
    def __init__(self, h, r=0, a=0, b=0):  # Constructor
        self.h = h
        self.r = r
        self.a = a
        self.b = b

    def surface_area(self):   # Virtual method
        raise NotImplementedError()

    def volume(self):         # Virtual method
        raise NotImplementedError()


class Cylinder(Figure):   # Derived class of cylinder
    def __init__(self, h, r):
        super().__init__(h, r=r)

    def surface_area(self):  # Overridden
        return 2*pi*self.r*(self.r + self.h)

    def volume(self):        # Overridden
        return pi*self.r**2*self.h


class Cone(Figure):   # Derived class of cone
    def __init__(self, h, r):
        super().__init__(h, r=r)

    def surface_area(self):  # Overridden
        l = (self.h**2+self.r**2)**0.5
        return pi*self.r*(self.r + l)

    def volume(self):        # Overridden
        return (1/3)*pi*self.r**2*self.h


class EllipticCylinder(Figure):   # Derived class of elliptic cylinder
    def __init__(self, h, a, b):
        super().__init__(h, a=a, b=b)

    def surface_area(self):  # Overridden
        sb = pi*(self.a+self.b)*self.h
        so = pi*self.a*self.b
        return sb+so

    def volume(self):        # Overridden
        return pi*self.a*self.b*self.h


class Menu:
    def __init__(self, choose):
        self.choose = choose

    def perform(self):
        if self.choose.strip() == '1':
            h = int(input("Type height: "))
            r = int(input("Type radius of base: "))
            cyl = Cylinder(h, r)
            print("Cylinder surface area:", round(cyl.surface_area(), 2))
            print("Cylinder volume:", round(cyl.volume(), 2))
            print()
        elif self.choose.strip() == '2':
            h = int(input("Type height: "))
            r = int(input("Type radius of base: "))
            cone = Cone(h, r)
            print("Cone surface area:", round(cone.surface_area(), 2))
            print("Cone volume:", round(cone.volume(), 2))
            print()
        elif self.choose.strip() == "3":
            h = int(input("Type height: "))
            a = int(input("Type big half-axis: "))
            b = int(input("Type small half-axis: "))
            ell = EllipticCylinder(h, a, b)
            print("Elliptic cylinder surface area:", round(ell.surface_area(), 2))
            print("Elliptic cylinder volume:", round(ell.volume(), 2))
            print()
        else:
            return "EXIT"


print("Laboratory work 6.1\nWritten by Hennadii Kochev, IP-91\nLanguage: Python 3")
print()
while True:
    print("Choose a figure:\n1.Cylinder (cyl)\n2.Cone (cone)\n3.Elliptic cylinder (ell)")
    choose = input("Your choose:")
    menu = Menu(choose)
    res =  menu.perform()
    if res == "EXIT": break




