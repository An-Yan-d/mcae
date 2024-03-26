import motion
import random
import points
from Commands import *
import numpy as np
import particletypes

tool = points.Utils()
shape = points.Shapes()


class VFP:
    def __init__(self,  position, speed,sigmap,sigmav=1,velocity=[0,0,0],tps=20,grav=40,air_resistance_factor=0.05):
        self.position = np.random.multivariate_normal(position, np.eye(3)*sigmap)
        v=np.random.multivariate_normal(velocity, np.eye(3)*sigmav)
        self.velocity = v*speed/np.linalg.norm(v)
        self.air_resistance_factor=air_resistance_factor
        self.tps=tps
        self.grav=grav*np.array([0,-1,0])

    def update(self):
        dt=1/self.tps

        # 计算空气阻力
        air_resistance = -self.air_resistance_factor * self.velocity  # 空气阻力与速度成正比（向上为负）

        # 计算加速度
        acceleration = (self.grav + air_resistance)

        # 更新速度和位置
        self.velocity += acceleration * dt
        self.position += self.velocity * dt

    def generate_trajectory(self, time_length):
        trajectory = []
        for _ in range(int(time_length)):
            trajectory.append(self.position.copy())
            self.update()
        return trajectory

def color_particle(color):
    return particletypes.ParticleType('ayparticle:life_color_gravity_particle',color=color,lifetime=1)


def fireworkline(t,p1,p2):
    """

    :param p:
    :param t:
    :param n:
    :param r:
    :param star:
    :param expl:
    :return:
    """
    default = particletypes.ParticleType('ayparticle:life_color_gravity_particle', color=(255, 255, 255), lifetime=10,
                                         lifetimerand=3, grav=5)
    motions=motion.CmdBuilder()
    l=shape.line(p1,p2,0.5)
    c0 = shape.randomPolyline(20, 0.15, l, 0.15, 0.5)
    c1 = shape.overbold(c0,4,0.015)
    c2 = shape.overbold(c0, 8,0.05)
    motions.static_particle(*t.time(offset=1), c1 ,*default)
    motions.static_particle(*t.time(), c2, *color_particle((255,100,100)))
    return motions.cmds

def fireworkball(t,p2,n):
    default = particletypes.ParticleType('ayparticle:life_color_gravity_particle', color=(255, 255, 255), lifetime=25,
                                         lifetimerand=3, grav=5)
    motions = motion.CmdBuilder()
    points=[]
    spds=[]
    for _ in range(n):
        vfp=VFP(p2,random.gauss(50,3),0.01,tps=30)
        traj=vfp.generate_trajectory(t.getduration())
        motions.static_particle(*t.time(offset=1), traj, *default)
        c1=shape.overbold(traj, 3, 0.01)
        motions.static_particle(*t.time(), c1, *color_particle((255, 100, 100)))
        points.append(traj[-1])
        spds.append((traj[-1]-traj[-2])/np.linalg.norm(traj[-1]-traj[-2]))
    return motions.cmds,points,spds

def fireworkfalling_individual(t,p,v,n):
    default = particletypes.ParticleType('ayparticle:life_color_gravity_particle', color=(255, 255, 255), lifetime=25,
                                         lifetimerand=3, grav=5)
    motions = motion.CmdBuilder()
    points=[]
    for _ in range(n):
        vfp=VFP(p,random.gauss(10,3),0.01,velocity=v,tps=30)
        traj=vfp.generate_trajectory(t.getduration())
        motions.static_particle(*t.time(), traj, *default)
        points.append(traj[-1])
    return motions.cmds,points

def fireworkfalling(t,points,spds,n):
    cmd=[]
    Points=[]
    for p,v in zip(points,spds):
        cmd1,points1=fireworkfalling_individual(t,p,v,n)
        cmd+=cmd1
        Points+=points1
    return cmd,Points

def fireworkflash(t,points,ratio):
    default = particletypes.ParticleType('ayparticle:life_color_gravity_particle', color=(255, 255, 255), lifetime=1,
                                        grav=5)
    motions = motion.CmdBuilder()
    r=0.94
    for tick in t.timelist():
        motions.static_particle(tick,tick, [np.random.multivariate_normal(p, np.eye(3)*0.5) for p in random.sample(points, int(ratio*len(points)))], *default)
        ratio*=r
    return motions.cmds

def firework(t,p1,p2,n1,n2,ratio):
    cmd1=fireworkline(t.subplan(0,50),p1,p2)
    cmd2,points1,spds=fireworkball(t.subplan(50,20),p2,n1)
    cmd3,points2 = fireworkfalling(t.subplan(70, 20),points1 ,spds, n2)
    cmd4=fireworkflash(t.subplan(100,30),points2,ratio)
    return cmd1+cmd2+cmd3+cmd4


if __name__=='__main__':
    from visualization import show_animation
    from schedule import schedule

    S = schedule()
    S.newplan(0, 100)
    show_animation(firework(S[0],[671,10,1550],[671,100,1550],100))
