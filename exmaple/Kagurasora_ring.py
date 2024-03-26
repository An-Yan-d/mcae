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

shape = points.Shapes()
tool = points.Utils()
DEFAULT = ('end_rod', 0, -1, 0, 9999, 0)

ring=shape.circle(0,2.2,0,0.3,0.2)
ring=tool.move_relative(ring)

motions = motion.CmdBuilder()

motions.static_particle(0,0, ring, *DEFAULT)


CMD=[]
for cmd in motions.cmds:
    CMD.append(ECmd({'at':'@e[tag=sora]','run':cmd},cmd.tick))

ani_func = function_generation.Function()
ani_func.add_cmd(CMD)
ani_func.save_seq_file('sora', namespace='mcae')

copy2there('Release', r'F:\mc\mc\.minecraft\versions\1.18.2-Fabric\saves\fireworktest\datapacks\fireworks\data\mcae\functions')
