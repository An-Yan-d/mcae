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

def add(p1,p2=center):
  rt=[]
  p1=shape.array_tran(p1)
  for p in p1:
    rt.append([p[0]+p2[0],p[1]+p2[1],p[2]+p2[2]])
  return rt

def char(c,p,t0,te,size,color="minecraft:dust 1 0.5 0.5 0.5",f=font.Font('files\hk4e_zh-cn.ttf')):
  h=28
  dt1=10
  
  dt2=140
  t=t0
  def coord_fun(t):
    t=t-t0
    return add(add([[t*(dt1-t)*math.sin(t)/200,t*h/10,t*(dt1-t)*math.cos(t)/200],[-t*(dt1-t)*math.sin(t)/200,t*h/10,-t*(dt1-t)*math.cos(t)/200]]),p)

  particle_cmd.cmds_fun(t0,t0+dt1,coord_fun,"minecraft:dust 1 1 2 0.5", 0, 0, 0, 0, 1,ppt=30)
  t=t0+dt1
  particle_cmd.static_particle(t, t,add(add([0,h,0]),p), 'minecraft:end_rod', 0, 0, 0, 0.2, 500)
  particle_cmd.static_particle(t, t,add(add([0,h,0]),p), 'minecraft:flash', 0, 0, 0, 1, 1)
  fireworks_char= f.point_generation(c,step=30,size=size)
  fireworks_char= add(add(add(fireworks_char),p),[-size/2,h-size/2,0])
  particle_cmd.motion_centre_spread(fireworks_char,t,t,"minecraft:end_rod",1)
  t+=10


  
  fireworks_char= add(fireworks_char,[0,0,0.001])
  def fun1(t):
    if t%2==0:
      return [0,0,0]
    return fireworks_char
  particle_cmd.cmds_fun(t,te, fun1,color, 0, 0, 0, 0, 1,ppt=1)
  t=t0

  particle_cmd.static_particle(te, te,  fireworks_char, 'minecraft:end_rod', 0, 0, 0, 0.5, 3)

char("毕",[-9.75,0,0],0,165,5)
char("业",[-3.25,0,0],5,165,5)
char("快",[3.25,0,0],10,165,5)
char("乐",[9.75,0,0],15,165,5)

char("I",[-13,0,0],185,350,4,color="minecraft:dust 1 1 0 0.5")
char("S",[-2.6,0,0],195,350,4,color="minecraft:dust 1 1 0 0.5")
char("J",[2.6,0,0],200,350,4,color="minecraft:dust 1 1 0 0.5")
char("T",[7.8,0,0],205,350,4,color="minecraft:dust 1 1 0 0.5")
char("U",[13,0,0],210,350,4,color="minecraft:dust 1 1 0 0.5")

char("^",[-9.0,0,0],190,350,4)


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
