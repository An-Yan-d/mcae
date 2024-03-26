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

def firework(t, p, n=800, speed=1.5,s=0.1):
    motions = motion.CmdBuilder()
    for i in range(n):
        motions.temp_cmds.append(
            motion.PCmd(0, 'minecraft:firework', *p, random.gauss(0, s), 0.5, random.gauss(0, s),
                        random.gauss(speed, 0.25), 0))
    motions.cmds_to_seq(*t.time())
    p[0] = 2 * 934 - p[0]
    for i in range(n):
        motions.temp_cmds.append(
            motion.PCmd(0, 'minecraft:firework', *p, random.gauss(0, s), 0.5, random.gauss(0, s),
                        random.gauss(speed, 0.25), 0))
    motions.cmds_to_seq(*t.time())
    motions.cmds.append(SCmd(t.time(0, 1, True)[0], p, 'minecraft:entity.firework_rocket.launch'))
    return motions.cmds

#
# def picture(t,center,pname):
#     default = ('end_rod', 0, 0, 0, 0, 1)
#     print(pname)
#     ps=shape.image_lossy(pname,5,center,0.2)
#     motions = motion.CmdBuilder()
#     center[1]-=15
#     motions.motion_spread_from_point(ps, *center, t.st, t.st, default[0], 1)
#     motions.cmds.append(SCmd(t.time(0, 0,True)[0], center,'minecraft:entity.firework_rocket.large_blast'))
#     return motions.cmds
#
# def char(c,t,p,s,f):
#     print(c)
#     default = ('end_rod', 0, 0, 0, 0, 1)
#     f=font.Font(f)
#     ps=f.point_generation(c,step=40,size=s)
#     motions=motion.CmdBuilder()
#     ps=tool.move(ps,*p)
#     p[1]-=10
#     motions.motion_spread_from_point(ps,*p, t.st,t.st, default[0], 1)
#     return motions.cmds
#
# def String(t,p,str,f,size=1.0):
#     n=len(str)
#     result=[]
#     d=1.1*size
#     sp1=p[0]-(n-1)/2*d
#     for i in range(n):
#         if str[i]!=' ':
#             result+=char(str[i],t,[sp1+i*d,85,132],size,f)
#     return result
#
# dic={'气泡柱奖':['Daydream'], '烤马铃薯奖':['KaguraSoraQAQ'],
# '咖啡奖':['__ART1st__','RektSuddenDeath','Unicorn'],
# '木斧奖':['xylotonium','SmartAngel','fish_Guo'],
# '齿轮奖':['RektSuddenDeath','Rinko'],
# '石英奖':['an_yan','Masane','xunfeng'],
# '铁栏杆奖':['kun_p','lytDARK','Wu_Zang']}
#
#
# def demo(i):
#     k=dic.keys()
#     string=list(k)[i]
#     S = schedule()
#     S.newplan(0, 60)
#     S.newplan(30, 60)
#     S.newplan(40, 60)
#
#     CMD = []
#     CMD += firework(S[0], [953, 75, -555]) + firework(S[0], [947, 75, -556]) + firework(S[0], [943, 75, -557])
#     CMD += picture(S[1], [935, 90, -556], str(i)+'.png')
#     CMD += String(S[1], [935, 85, -559], string, 'hk4e_zh-cn.ttf')
#     if len(dic[string])==1:
#         CMD += String(S[2], [935, 81, -559], dic[string][0], 'Gabriola.ttf', 0.5)
#     if len(dic[string])==2:
#         CMD += String(S[2], [937, 81, -559], dic[string][0], 'Gabriola.ttf', 0.5) \
#     + String(S[2], [933, 81, -559], dic[string][1], 'Gabriola.ttf', 0.5)
#     if len(dic[string])==3:
#         CMD += String(S[2], [935, 81, -559], dic[string][0], 'Gabriola.ttf', 0.5)+\
#                String(S[2], [937, 81, -559], dic[string][1], 'Gabriola.ttf', 0.5) \
#             + String(S[2], [933, 81, -559], dic[string][2], 'Gabriola.ttf', 0.5)
#
#     return CMD
#

S = schedule()
S.newplan(1, 60)

ani_func = function_generation.Function()

CMD=firework(S[0], [953, 75, -555]) + firework(S[0], [947, 75, -556]) + firework(S[0], [943, 75, -557])
ani_func.add_cmd(CMD)
ani_func.save_seq_file('firework', namespace='mcae')
copy2there('../Release', r'F:\mc\SJMC Meeting 3\.minecraft\saves\world'
                      r'\datapacks\fireworks\data\mcae\functions')