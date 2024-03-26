def hex2decimal(hex_number):
    decimal_number = int(hex_number, 16)
    return decimal_number


class ParticleType:
    def __init__(self, name, color, lifetime, lifetimerand=0, grav=1, x=0, y=0, z=0, speed=0, amount=1):
        self.name = name
        if type(color) == str:
            self.color = hex2decimal(color)
        else:
            self.color = (color[0] << 16) + (color[1] << 8) + color[2]
        self.lifetime = lifetime
        self.lifetimerand = lifetimerand
        self.grav = grav
        self.x = x
        self.y = y
        self.z = z
        self.speed = speed
        self.amount = amount

    def __iter__(self):
        return iter([
        f"{self.name} {self.color} {self.lifetime} {self.lifetimerand} {self.grav}", self.x, self.y, self.z, self.speed,
        self.amount])

    def __str__(self):
        return f"{self.name} {self.color} {self.lifetime} {self.lifetimerand} {self.grav}"

