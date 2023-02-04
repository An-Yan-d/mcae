class PCmd:
    def __init__(self, tick, name, x, y, z, dx, dy, dz, speed, amount, mode='force'):
        self.tick = tick
        self.name = name
        self.x = round(x, 2)
        self.y = round(y, 2)
        self.z = round(z, 2)
        self.dx = round(dx, 2)
        self.dy = round(dy, 2)
        self.dz = round(dz, 2)
        self.speed = speed
        self.amount = amount
        self.mode = mode

    def __str__(self):
        text = 'particle %s %s %s %s %s %s %s %s %s %s' \
               % (self.name, self.x, self.y, self.z, self.dx, self.dy, self.dz, self.speed, self.amount, self.mode)
        return text

class SCmd:
    def __init__(self, tick, p,stype,r=999.0,etype='ambient',object='@a'):
        self.tick = tick
        self.stype = stype
        self.etype = etype
        self.object = object
        self.x = round(p[0], 2)
        self.y = round(p[1], 2)
        self.z = round(p[2], 2)
        self.r = round(r, 2)


    def __str__(self):
        text='playsound %s %s %s %f %f %f %f' \
             % (self.stype,self.etype,self.object,self.x, self.y, self.z, self.r)
        return text