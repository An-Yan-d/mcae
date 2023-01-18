import particle
import function_generation
import points
import font
import math
import numpy as np


shape = points.Shapes()
particle_cmd = particle.CmdBuilder()
ani_func = function_generation.Function()

center=[-1643,8,43]


def coord_fun(t):
  return [[t*(10-t)*math.sin(t)/200,t*45/20,t*(10-t)*math.cos(t)/200],[-t*(10-t)*math.sin(t)/200,t*45/20,-t*(10-t)*math.cos(t)/200]]

particle_cmd.cmds_fun(0,20,coord_fun,"minecraft:end_rod", 0, 0, 0, 0, 1,ppt=5)
particle_cmd.static_particle(20, 20,[[0,45,0]], 'minecraft:end_rod', 0, 0, 0, 2, 1000)
f=font.Font(r'files\hk4e_zh-cn.ttf')
fireworks_string= f.string_generation("毕业快乐",step=20,size=5,distance=5*1.3)
fireworks_string=shape.move(fireworks_string,-5*2.45,80-2.5,0)


particle_cmd.motion_centre_spread(fireworks_string,20,20,"minecraft:end_rod",1)
fireworks_string=shape.move(fireworks_string,0,0,0.001)
particle_cmd.static_particle(55, 55, fireworks_string, 'minecraft:end_rod', 0, 0, 0, 0, 1)
particle_cmd.static_particle(75, 75, fireworks_string, 'minecraft:end_rod', 0, 0, 0, 0, 1)
particle_cmd.static_particle(95, 95, fireworks_string, 'minecraft:end_rod', 0, 0, 0, 0.5, 3)

ani_func.add_cmd(particle_cmd.cmds)
ani_func.save_seq_file('firework', build_schedule=True, namespace='mcae')
#/function mcae:firework/schedule
#/particle minecraft:firework ^ ^1 ^2 0 0 0 0 1 force

# interval=[]
# for i in range(16384):
#     interval.append([0,-128,0])
# mid=shape.get_midpoint(fireworks_string)
# def coord_fun(t):
#     T1=40
#     if(t%2==0):
#         return interval
#     if(t<T1):
#         pts=[]
#         for p in fireworks_string:
#             pts.append([mid[0]*(1-t/T1)+p[0]*t/T1,mid[1]*(1-t/T1)+p[1]*t/T1,mid[2]*(1-t/T1)+p[2]*t/T1])
#         return pts
#     return fireworks_string



# particle_cmd.cmds_fun(0,80,coord_fun,"minecraft:end_rod", 0, 0, 0, 0, 1,ppt=7)

#print(fireworks_string)
