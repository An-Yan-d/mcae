import motion
import function_generation
import points

import visualization as vs

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

""" if axr=='equal':
        dx=max(x)-min(x)
        dy=max(y)-min(y)
        dz=max(z)-min(z)
        r=0.1

        d=(0.5+r)*max([dx,dy,dz])

        ax.set_xlim3d(xmin=min(x)+0.5*dx-d,xmax=max(x)-0.5*dx+d)
        ax.set_ylim3d(ymin=min(y)+0.5*dy-d,ymax=max(y)-0.5*dy+d)
        ax.set_zlim3d(zmin=min(z)+0.5*dz-d,zmax=max(z)-0.5*dz+d)"""

def sum(x,*a):
    if a:
        for num in a:
            x+=num
    return x
print(sum(1,2,3))

def func(fun,*a):
    print(fun)
    return fun(*a)

print(func(sum,1,3,5))    

def test1(x,y,z):
    print(x,y,z)
    return
print(np.array([1,2,3])*2)

test1(*(np.array([1,2,3])*2))

print(type([])==list)

def test2(n="x",*name,type="default"):
    print(name,type,n)
    

test2(1,2,3,4)
print(list(([1,2,3],)))

tool=points.Shapes()
print(tool.coordinate_transformation([0,-1,0],[1,0,1],[-1,0,2**0.5]))
print([np.array([1,2,3])])
x,y=tool.Coordinate_transformation([1,1,1],[-1,1,0],[[4,1,-1],[1,5,9]])
print(x,y)
print(np.inner(x,y))
print(tool.cub(1,1,1,n1=[1,1,1],n2=[-1,1,0],step=0.1))
vs.show_static(tool.cub(1,1,1,n1=[1,1,1],n2=[-1,1,0],step=0.1))
print('---------------------------------')
lis=[1,2]

print('---------------------------------')
# f=vs.show_static(tool.bezier3x_xyz([[1,0,3],[4,5,-5],[-6,0,8],[7,-4,9],[6,0,-6]],0.2),show='off')
# vs.show_static([[1,0,3],[4,5,-5],[-6,0,8],[7,-4,9],[6,0,-6]],ax=f,color='red')
# vs.show_static(tool.parabola([-4,5,7],[4,5,1],0.1))



shape = points.Shapes()
particle_cmd = particle.CmdBuilder()
ani_func = function_generation.Function()
# line = shape.line([0, 0, 0], [20, 20, 20], 0.2)
# # 生成静态的粒子命令，动画从0Tick开始至20Tick结束，点使用上面生成的直线，粒子名为'end_rod'，
# # 粒子运动范围为0, 0, 0， 速度为0， 每条指令产生1个粒子
# particle_cmd.static_particle(0, 20, line, 'end_rod', 0, 0, 0, 0, 1)
# # 将上面生成的粒子命令添加到function中，如果制作了多个粒子动画，每个都会保存在particle_cmd.cmds中，只需要在最后添加一次即可
# vs.show_animation(particle_cmd.cmds)

curve = shape.bezier3x_xyz([[21, 20, 20], [38, 28, 8], [46, 19, 10]], 0.2)
vs.show_static(curve)
particle_cmd.static_particle(0, 40, curve, 'end_rod', 0, 0, 0, 0, 1)

particle_cmd.cls()

# 这次换点不一样子粒子
def fun(t):
    return t**2
helix = shape.helix_fun(fun,curve)
particle_cmd.static_particle_fun(0, 40, helix, 'end_rod', 0.1, 0.1, 0.1, 0.03, 3,fun)

vs.show_animation(particle_cmd.cmds)
particle_cmd.cls()
# vs.show_static(helix)
# vs.show_animation(particle_cmd.cmds,t0=20)

def coord_fun(t):
    t=10*t
    x=t*math.sin(t)
    y=t*math.cos(t)
    z=t
    return x,y,z

particle_cmd.cmds_fun(0,40,coord_fun,'end_rod', 0.1, 0.1, 0.1, 0.03, 1,ppt=7)
vs.show_animation(particle_cmd.cmds)
particle_cmd.cls()

def cfun(t):
    p=tool.cub(1,1,1,a=t/20,step=0.1,n1=[1,1,1],n2=[-1,1,0])
    return p

particle_cmd.cmds_fun(10,40,cfun,'end_rod', 0.1, 0.1, 0.1, 0.03, 1,ppt=7)
# vs.show_animation(particle_cmd.cmds)


