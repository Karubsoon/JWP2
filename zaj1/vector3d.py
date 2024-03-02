import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Składowa x: {self.x}, Składowa y: {self.y}, Składowa z: {self.z}"

    def get_x(self):
        return self.x
    def set_x(self, value):
        self.x = value
    def get_y(self):
        return self.y
    def set_y(self, value):
        self.y = value
    def get_z(self):
        return self.z
    def set_z(self, value):
        self.z = value

    @staticmethod
    def norm(x, y, z):
        return math.sqrt(x^2+y^2+z^2)


x = float(input('Podaj x = '))
y = float(input('Podaj x = '))
z = float(input('Podaj x = '))


wektor = Vector3D(3, 4, 5)
print(wektor)

print(wektor.norm(x,y,z))




