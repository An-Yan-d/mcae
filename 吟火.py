import motion
import function_generation
import points
import util
from util import copy2there
import random
import font
import numpy as np
import cv2
from Commands import *
from schedule import *
from particletypes import *
from fireworks import *


util.delete_folder_contents('Release')

shape = points.Shapes()
tool = points.Utils()



S=schedule()
S.newplan(0, 130)
S.setnewgroupstart(800)

CMD=[]
CMD+=firework(S[0],[671,10,1550],[670,100,1551],200,5,0.4)


ani_func = function_generation.Function()
ani_func.add_cmd(CMD)
ani_func.save_seq_file('firework_yinhuo', namespace='mcae')

copy2there(r'Release', r'F:\mc\MC\.minecraft\versions\1.20.4-fabric\saves\sjtu\datapacks\fireworks\data\mcae\functions')
