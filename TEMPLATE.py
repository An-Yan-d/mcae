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
from particletypes import *

shape = points.Shapes()
tool = points.Utils()


default = ParticleType('ayparticle:life_color_gravity_particle',color=(255,255,255),lifetime=100)






S=schedule()
S.newplan(0, 800)
S.setnewgroupstart(800)

CMD=[]


ani_func = function_generation.Function()
ani_func.add_cmd(CMD)
ani_func.save_seq_file('firework_yinhuo', namespace='mcae')

copy2there('../Release', r'C:\Program Files (x86)\MC\mc\.minecraft\versions\1.20.4-fabric\saves\sjtu\datapacks\fireworks\data\mcae\functions')
