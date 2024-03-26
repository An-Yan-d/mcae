import motion
import function_generation
import points
from util import copy2there
import random
import font
import numpy as np
import cv2
from Commands import *
from schedule import *
import csv

shape = points.Shapes()
tool = points.Utils()
DEFAULT = ('end_rod', 0, -1, 0, 9999, 0)

# wing=np.array(list(csv.reader(open(r'files/wings.csv'),quoting=2)))
#
# mid=np.average(wing,axis=0)
# wing=wing-mid
# scale=np.max(np.max(wing,axis=0)-np.min(wing,axis=0))
# wing=wing/scale*2
# wing=wing-np.min(wing,axis=0)
# wing=wing.tolist()
# print(np.min(wing,axis=0),np.max(wing,axis=0))
# K=5
# points=np.zeros(np.array(np.max(wing,axis=0)*K+1,dtype=np.uint8))
# print(points.shape)
# for p in wing:
#     points[int(p[0]*K),int(p[1]*K),int(p[2]*K)]+=1
# points=np.argwhere(points>4000)/K
# print(points)

coord=[[14,122],[37,100],[51,89],[64,75],[75,50],[92,22]
    ,[111,14],[139,11],[181,28],[223,50],[284,74],[334,89],
        [388,94],[352,114],[318,119],[289,118],[390,133],[345,147]
        ,[309,157],[331,169],[356,176],[306,185],[262,172],[223,156],
        [238,179],[258,198],[276,213],[227,203],[198,186],[205,208],
        [190,201],[200,226],[176,215],[152,193],[138,177],[109,157],
       [125,197],[100,177],[103,201],[82,191],[80,224],[73,255],[45,199]
       ]
points=[]
for c in coord:
    points.append([c[0]/200,(266-c[1])/200,-0.3])
    points.append([-c[0] / 200, (266 - c[1]) / 200, -0.3])
points=tool.move(points,0,0.8,0)
points=tool.move_relative(points)

motions = motion.CmdBuilder()

motions.static_particle(0,0, points, *DEFAULT)


CMD=[]
for cmd in motions.cmds:
    CMD.append(ECmd({'at':'@e[tag=sora]','run':cmd},cmd.tick))

ani_func = function_generation.Function()
ani_func.add_cmd(CMD)
ani_func.save_seq_file('sora', namespace='mcae',build_schedule=False)

copy2there('Release', r'F:\mc\mc\.minecraft\versions\1.18.2-Fabric\saves\fireworktest\datapacks\fireworks\data\mcae\functions')
