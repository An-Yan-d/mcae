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

globalt = 0






shape = points.Shapes()
tool = points.Utils()


def roof1(t):
    default = ('end_rod', 0, 0, 0, 0, 1)
    # 粒子相关
    # 初始化形状，粒子命令生成器，函数生成器

    # z=129.5
    z = 130
    l1 = shape.line([369, 64, z], [390.5, 64, z], 0.5)
    b1 = shape.bezier3x_xyz([[390.5, 64, z], [390, 65, z], [388, 66.2, z], [386, 68, z],
                             [382.5, 68.5, z], [376, 68.8, z], [357.5, 69.4, z],
                             [354.5, 69.5, z], [353.5, 69.5, z], [351.5, 68.5, z], [350.5, 67.5, z], [349.5, 66.2, z],
                             [347.5, 67, z], [346.5, 66.5, z], [347.5, 65.5, z], [348.5, 64.5, z]], 0.5)

    points1 = l1 + b1  # 屋顶横向
    motions1 = motion.CmdBuilder()
    motions1.static_particle(*t.time(0, 0.4), points1, *default)

    motions2 = motion.CmdBuilder()  # 房檐四个角
    b2 = shape.bezier3x_xyz(
        [[348.5, 64.5, z], [345.5, 61, 126.5], [341.5, 58.8, 122.5], [336, 56.5, 117], [330.5, 55.5, 111.5]
            , [329, 56.5, 110]], 0.5)
    motions2.static_particle(*t.time(0.4, 0.6), b2, *default)
    b2 = shape.bezier3x_xyz(
        [[338, 47, 119], [334, 45.4, 115], [330, 44, 111], [325.5, 43, 106.5], [324, 44.5, 105]], 0.5)
    motions2.static_particle(*t.time(0.4, 0.6), b2, *default)

    b3 = shape.bezier3x_xyz([[329, 56.5, 110], [329.5, 55, 144.5], [329.5, 55, 133], [329.5, 55, z]], 0.5)
    motions2.static_particle(*t.time(0.6, 1), b3, *default)
    b4 = shape.bezier3x_xyz([[329, 56.5, 110], [397.5, 54.5, 110.5], [377.5, 54.5, 110.5], [370, 54.5, 110.5]], 0.5)
    motions2.static_particle(*t.time(0.6, 1), b4, *default)

    b3 = shape.bezier3x_xyz([[324, 44.5, 105], [324.5, 43, 149.5], [324.5, 43, 133], [324.5, 43, z]], 0.5)
    motions2.static_particle(*t.time(0.6, 1), b3, *default)
    b4 = shape.bezier3x_xyz([[324, 44.5, 105], [400.5, 42.5, 105.5], [377.5, 42.5, 105.5], [370, 42.5, 105.5]], 0.5)
    motions2.static_particle(*t.time(0.6, 1), b4, *default)

    motions2.mirror('z', z)

    motions = motion.CmdBuilder()
    motions.cmds = motions1.cmds + motions2.cmds
    motions.mirror('x', 370.5)

    return motions.cmds


def roof2(t):
    default = ('end_rod', 0, 0, 0, 0, 1)
    motions1 = motion.CmdBuilder()
    b = shape.bezier3x_xyz([[349.5, 62, 131.5], [347.5, 60.5, 134.2], [343, 57.4, 139],
                            [337.5, 55.2, 145.2], [333.2, 55, 149]], 0.6)
    motions1.static_particle(*t.time(0.4, 1), b, *default)

    tmp_cmds = motions1.cmds.copy()
    for cmd in tmp_cmds:
        for i in range(1, 11):
            motions1.cmds.append(
                motion.PCmd(cmd.tick, cmd.name, cmd.x + i * (370.5 - cmd.x) / 10.5, cmd.y, cmd.z, cmd.dx, cmd.dy,
                            cmd.dz, cmd.speed, cmd.amount,
                            cmd.mode))

    motions2 = motion.CmdBuilder()
    b = shape.bezier3x_xyz([[339.5, 47.5, 141.5], [336.8, 45.5, 145.3], [333, 44, 149.2], [327, 43, 153.5]], 0.6)
    motions2.static_particle(*t.time(0.4, 1), b, *default)

    tmp_cmds = motions2.cmds.copy()
    for cmd in tmp_cmds:
        for i in range(1, 16):
            motions2.cmds.append(
                motion.PCmd(cmd.tick, cmd.name, cmd.x + i * (370.5 - cmd.x) / 15.5, cmd.y, cmd.z, cmd.dx, cmd.dy,
                            cmd.dz, cmd.speed, cmd.amount,
                            cmd.mode))

    motions = motion.CmdBuilder()
    motions.cmds = motions1.cmds + motions2.cmds
    motions.mirror('x', 370.5)

    return motions.cmds


def roof3(t):
    default = ('end_rod', 0, 0, 0, 0, 1)
    # 粒子相关
    # 初始化形状，粒子命令生成器，函数生成器

    # z=129.5

    l1 = shape.line([290.5, 55.5, 136.5], [290.5, 55.5, 151.5], 0.6)
    b1 = shape.bezier3x_xyz([[290.5, 55.5, 151.5], [290.5, 56, 152.2], [290.5, 57.5, 150.5], [290.5, 58.5, 151.5]
                                , [290.5, 55.5, 152.5]], 0.6)

    points1 = l1 + b1  # 屋顶横向
    motions1 = motion.CmdBuilder()
    motions1.static_particle(*t.time(0, 0.4), points1, *default)

    motions2 = motion.CmdBuilder()  # 房檐四个角
    b2 = shape.bezier3x_xyz(
        [[290.5, 55.5, 152.5], [293.5, 53.5, 152.5], [297.5, 51.5, 152.5], [300.5, 49.5, 152.5], [303.5, 48.5, 155.5],
         [306.5, 49.5, 158.5]], 0.6)
    motions2.static_particle(*t.time(0.4, 0.6), b2, *default)
    b2 = shape.bezier3x_xyz(
        [[306.5, 49.5, 158.5], [306.5, 48, 152], [306.5, 48, 146], [306.5, 48, 137.5]], 0.6)
    motions2.static_particle(*t.time(0.6, 1), b2, *default)
    b2 = shape.bezier3x_xyz(
        [[306.5, 49.5, 158.5], [301.5, 48, 158.5], [295.5, 48, 158.5], [290.5, 48, 158.5]], 0.6)
    motions2.static_particle(*t.time(0.6, 1), b2, *default)

    motions2.mirror('x', 290.5)

    motions = motion.CmdBuilder()
    motions.cmds = motions1.cmds + motions2.cmds
    motions.mirror('z', 137.5)
    motions.mirror('x', 370.5)
    return motions.cmds


def roof4(t):
    default = ('end_rod', 0, 0, 0, 0, 1)
    # 粒子相关
    # 初始化形状，粒子命令生成器，函数生成器
    motions1 = motion.CmdBuilder()
    l1 = shape.line([290.5, 63.5, 222.5], [290.5, 63.5, 235.5], 0.6)
    b1 = shape.bezier3x_xyz([[290.5, 63.5, 151.5 + 84], [290.5, 64, 152.2 + 84], [290.5, 65.5, 150.5 + 84],
                             [290.5, 66.5, 151.5 + 84]
                                , [290.5, 63.5, 152.5 + 84]], 0.6)
    points1 = l1 + b1  # 屋顶横向
    motions1.static_particle(*t.time(0, 0.4), points1, *default)

    l1 = shape.line([290.5, 63.5 - 12, 238], [290.5, 63.5 - 12, 259.5], 0.6)
    b1 = shape.bezier3x_xyz(
        [[290.5, 63.5 - 12, 151.5 + 108], [290.5, 64 - 12, 152.2 + 108], [290.5, 65.5 - 12, 150.5 + 108],
         [290.5, 66.5 - 12, 151.5 + 108]
            , [290.5, 63.5 - 12, 152.5 + 108]], 0.6)
    points1 = l1 + b1  # 屋顶横向
    motions1.static_particle(*t.time(0, 0.4), points1, *default)

    motions2 = motion.CmdBuilder()  # 房檐四个角
    b2 = shape.bezier3x_xyz(
        [[290.5, 63.5, 152.5 + 84], [293.5, 61.5, 152.5 + 84], [297.5, 59.5, 152.5 + 84], [300.5, 57.5, 152.5 + 84],
         [303.5, 56.5, 155.5 + 84],
         [306.5, 57.5, 158.5 + 84]], 0.6)
    motions2.static_particle(*t.time(0.4, 0.6), b2, *default)
    b2 = shape.bezier3x_xyz(
        [[306.5, 57.5, 158.5 + 84], [306.5, 56, 152 + 84], [306.5, 56, 146 + 84], [306.5, 56, 223.5]], 0.6)
    motions2.static_particle(*t.time(0.6, 1), b2, *default)
    b2 = shape.bezier3x_xyz(
        [[306.5, 57.5, 158.5 + 84], [301.5, 56, 158.5 + 84], [295.5, 56, 158.5 + 84], [290.5, 56, 158.5 + 84]], 0.6)
    motions2.static_particle(*t.time(0.6, 1), b2, *default)

    b2 = shape.bezier3x_xyz(
        [[290.5, 63.5 - 12, 152.5 + 108], [293.5, 61.5 - 12, 152.5 + 108], [297.5, 59.5 - 12, 152.5 + 108],
         [300.5, 57.5 - 12, 152.5 + 108], [303.5, 56.5 - 12, 155.5 + 108],
         [306.5, 57.5 - 12, 158.5 + 108]], 0.6)
    motions2.static_particle(*t.time(0.4, 0.6), b2, *default)
    b2 = shape.bezier3x_xyz(
        [[306.5, 57.5 - 12, 158.5 + 108], [306.5, 56 - 12, 152 + 108], [306.5, 56 - 12, 146 + 108],
         [306.5, 56 - 12, 237.5]], 0.6)
    motions2.static_particle(*t.time(0.6, 1), b2, *default)
    b2 = shape.bezier3x_xyz(
        [[306.5, 57.5 - 12, 158.5 + 108], [301.5, 56 - 12, 158.5 + 108], [295.5, 56 - 12, 158.5 + 108],
         [290.5, 56 - 12, 158.5 + 108]], 0.6)
    motions2.static_particle(*t.time(0.6, 1), b2, *default)

    b2 = shape.bezier3x_xyz(
        [[302.5, 47.5, 237.5], [303.5, 47, 237.5], [306.5, 46.2, 240.5], [308.5, 47.5, 242.5]], 0.6)
    motions2.static_particle(*t.time(0.4, 0.6), b2, *default)
    b2 = shape.bezier3x_xyz(
        [[308.5, 47.5, 242.5], [308.5, 46, 236.5], [308.5, 46, 230.5], [308.5, 46, 222.5]], 0.6)
    motions2.static_particle(*t.time(0.6, 1), b2, *default)
    b2 = shape.bezier3x_xyz(
        [[308.5, 47.5, 242.5], [304.5, 46, 242.5], [302.5, 46, 242.5], [300.5, 46, 242.5]], 0.6)
    motions2.static_particle(*t.time(0.6, 1), b2, *default)

    motions2.mirror('x', 290.5)

    motions = motion.CmdBuilder()
    motions.cmds = motions1.cmds + motions2.cmds
    motions.mirror('z', 223.5)
    motions.mirror('x', 370.5)
    return motions.cmds


def ROOF(t):
    return roof1(t) + roof3(t) + roof4(t)


ani_func = function_generation.Function()


def ring(t):
    center = [370.5, 8, 223.5]
    default = ('end_rod', 0, -1, 0, 999, 0)
    c1 = shape.bezier3x_xyz([center, [374.5, 8, 223], [377, 8, 222.5], [380, 8, 220]
                                , [381.5, 8, 215.2], [380.3, 8, 211.4], [377.5, 8, 207.5]], 0.8)

    c2 = shape.bezier3x_xyz([[377.5, 8, 207.5], [384.6, 8, 213.2], [387.4, 8, 220]
                                , [387, 8, 228.5]], 0.8)
    c3 = shape.bezier3x_xyz([[387, 8, 228.5], [387, 8, 225.4], [386.5, 8, 223]
                                , [385.5, 8, 221]], 0.8)
    c4 = shape.bezier3x_xyz([[385.5, 8, 221], [384.2, 8, 225.2], [379, 8, 230]
                                , [373.5, 8, 229.5]], 0.8)
    c5 = shape.bezier3x_xyz([[373.5, 8, 229.5], [376, 8, 226.4], [372.5, 8, 224.5]
                                , center], 0.8)
    l1 = shape.line_link([[370.5, 8, 196.5], [343.5, 8, 223.5], [370.5, 8, 250.5], [397.5, 8, 223.5]], 0.8)
    l1 = tool.move(l1, -370.5, -8, -223.5)
    p1 = c1 + c2 + c3 + c4 + c5
    p1 = tool.move(p1, -370.5, -8, -223.5)
    p2 = tool.rotate(0, 1, 0, 120, p1)
    p3 = tool.rotate(0, 1, 0, 240, p1)
    points = p1 + p2 + p3 + l1

    def ring_fun(t):
        ps = tool.rotate(0, 1, 0, t / 2, points)
        if t / 10 < 26:
            return tool.move(ps, 370.5, 9 + t / 10, 223.5)
        else:
            return tool.move(ps, 370.5, 35, 223.5)

    motions_ring = motion.CmdBuilder()
    motions_ring.cmds_fun(*t.time(0, 1), ring_fun, *default, ppt=1)
    return motions_ring.cmds


def firework2(t, p, n=1200, speed=2,offset=0.0,s=0.1):
    motions = motion.CmdBuilder()
    for i in range(n):
        motions.temp_cmds.append(
            motion.PCmd(0, 'minecraft:firework', *p, random.gauss(0.25 + offset, s), 1, random.gauss(0.25, s),
                        random.gauss(speed, 0.25), 0))
    motions.cmds_to_seq(*t.time())
    p[0] = 2 * 370.5 - p[0]
    for i in range(n):
        motions.temp_cmds.append(
            motion.PCmd(0, 'minecraft:firework', *p, random.gauss(-0.25 - offset, s), 1, random.gauss(0.25, s),
                        random.gauss(speed, 0.25), 0))
    motions.cmds_to_seq(*t.time())
    return motions.cmds

def firework3(t, p, n=15000, speed=8):
    motions = motion.CmdBuilder()
    for i in range(n):
        motions.temp_cmds.append(
            motion.PCmd(0, 'minecraft:end_rod', *p, random.gauss(-0.5, 0.25), 1, 0,
                        random.gauss(speed, 0.5), 0))
    motions.cmds_to_seq(*t.time())
    p[0] = 2 * 370.5 - p[0]
    for i in range(n):
        motions.temp_cmds.append(
            motion.PCmd(0, 'minecraft:end_rod', *p, random.gauss(0.5, 0.25), 1, 0,
                        random.gauss(speed, 0.5), 0))
    motions.cmds_to_seq(*t.time())
    return motions.cmds


def firework(p,t,n,r,star=True,expl=False):
    default = ('end_rod', 0, 0, 0, 0, 1)
    motions1=motion.CmdBuilder()
    l=shape.line([p[0],7,p[2]],p,0.5)
    c1 = shape.helix([0, 0, 0], [0, 0, 0], 0.4, 0.5, 0, 'custom', l, False)
    c2 = shape.helix([0, 0, 0], [0, 0, 0], 0.4, 0.5, 120, 'custom', l, False)
    c3 = shape.helix([0, 0, 0], [0, 0, 0], 0.4, 0.5, 240, 'custom', l, False)
    motions1.static_particle(*t.time(0, 0.3,True),c1,*default)
    motions1.static_particle(*t.time(0, 0.3,True), c2, *default)
    motions1.static_particle(*t.time(0, 0.3,True), c3, *default)

    points1=[]
    for i in range(n):
        points1+=tool.move([np.array(tool.vec_unit([random.gauss(0,1),random.gauss(0,1),random.gauss(0,1)]))*r],*p)
    motions1.motion_spread_from_point(points1,*p,*t.time(0.4,0.4,True),default[0],1)
    motions1.cmds.append(SCmd(t.time(0.4,0.4,True)[0],p,'minecraft:entity.firework_rocket.large_blast_far'))
    if star:
        for i in range(24):
            point=tool.vec_unit([random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1)])
            l2=shape.line([0,0,0],np.array(point)*1.5*r,1.5)
            l2=tool.move(l2,*p)
            motions1.static_particle(*t.time(0.4,0.6,True),l2,*default)

    if expl:
            motions1.static_particle(*t.time(1,1,True),points1,'minecraft:firework',0,0,0,0.2,10)
            motions1.cmds.append(SCmd(t.time(1, 1,True)[0], p,'minecraft:entity.firework_rocket.twinkle_far'))

    return motions1.cmds

def firework4(t,type):
    if type ==1:
        return firework([455, 80, 111], t, 200, 10) + firework([286, 80, 111], t, 200, 10) \
            + firework([490, 100, 164], t, 400, 15) + firework([251, 100, 164], t, 400, 15) \
        + firework([486, 92, 213], t, 200, 10) + firework([255, 92, 213], t, 200, 10)
    if type==2:
        return firework([484, 75, 184], t, 200, 15) + firework([257, 70, 184], t, 200, 15) \
            + firework([475, 140, 97], t, 400, 20) + firework([266, 140, 97], t, 400, 20) \
            + firework([428, 100, 85], t, 200, 10) + firework([313, 100, 85], t, 200, 10)

def Firework(t,flag=True):
    k=1
    if flag:
        k=2
    t22 = plan(0*k+t.st, 100)
    t23 = plan(20*k+t.st, 100)
    t24 = plan(40*k+t.st, 100)
    t25 = plan(60*k+t.st, 100)
    t26 = plan(80*k+t.st, 100)

    return firework([361, 110, 100], t22, 1000, 30,expl=flag) + firework([398, 90, 105], t23, 500, 15,expl=flag) \
    + firework([347, 74, 101], t24, 800, 22,expl=flag) + firework([399, 105, 90], t25, 1000, 30,expl=flag) \
    + firework([329, 103, 97], t26, 800, 22,expl=flag)

def char(c,t,p,s=12):
    p[0]-=4
    print(c)
    default = ('end_rod', 0, 0, 0, 0, 1)
    f=font.Font(r'../files/演示悠然小楷.ttf')
    ps=f.point_generation(c,step=25,size=s)
    motions=motion.CmdBuilder()
    ps=tool.move(ps,*p)
    motions.motion_spread_from_point(ps, p[0],54,p[2]-20, t,t, default[0], 1)
    motions.static_particle(t+50,t+50,ps,*default)
    return motions.cmds

def String1(t):
    return char('沪',t.st+0,[350.5,95,132])+char('上',t.st+2,[360.5,95,132])+char('云',t.st+4,[370.5,95,132])\
        +char('相',t.st+6,[380.5,95,132])+char('聚',t.st+8,[390.5,95,132])+char('玉',t.st+10,[350.5,80,132])\
        +char('衡',t.st+12,[360.5,80,132])+char('共',t.st+14,[370.5,80,132])+char('迎',t.st+16,[380.5,80,132])\
        +char('春',t.st+18,[390.5,80,132])

def String2(t):
    # char('2',t.st+0,[340.5,95,132],20)+char('0',t.st+3,[360.5,95,132],20)+char('2',t.st+6,[380.5,95,132],20)\
    #         +char('3',t.st+9,[400.5,95,132],20)+
    return char('新',t.st+12,[340.5,80,132],20)\
        +char('年',t.st+15,[360.5,80,132],20)+char('快',t.st+18,[380.5,80,132],20)+char('乐',t.st+21,[400.5,80,132],20)

def picture(t,hsize,center,step=0.5):
    default = ('end_rod', 0, 0, 0, 0, 1)
    img=cv2.imread(r'../files/VCG211387809830-1.jpg', 0)
    points=[]
    (h,w)=img.shape
    ratio=w/h
    wsize=ratio*hsize
    nx=int(wsize/step)
    ny=int(hsize/step)
    for i in range(nx):
        for j in range(ny):
            if img[int(j/ny*h)][int(i/nx*w)]>128:
                points.append([i*step-wsize/2,-j*step+hsize/2,0])
    motions = motion.CmdBuilder()
    ps = tool.move(points, *center)
    motions.motion_spread_from_point(ps, center[0], 54, center[2] - 20, t.st+21, t.st+21, default[0], 1)
    motions.static_particle(t.st+71, t.st+71, ps, *default)
    return motions.cmds



S=schedule()
# t = schedule(,)
S.newplan(0, 800)
S.newgroupstart(800)
S.newplan(0, 100)
S.newplan(70, 95)
S.newplan(140, 90)
S.newplan(210, 80)
S.newplan(280, 60)
S.newplan(350, 50)
S.newplan(410, 45)
S.newplan(470, 40)
S.newplan(520, 35)
S.newplan(565, 30)
S.newplan(610, 30)
S.newgroupstart(1410)
S.newplan(0, 150)
S.newplan(10, 150)
S.newplan(20, 150)
S.newplan(30, 150)
S.newplan(40, 150)
S.newplan(50, 150)
S.newplan(60, 150)
S.newplan(70, 150)
S.newplan(80, 150)
S.newgroupstart(1590)
S.newplan(0, 150)

S.newgroupstart(1740)
S.newplan(0,100,'22_')
S.newplan(90,100,'23_')
S.newplan(50,100)
S.newplan(150,100)

S.newgroupstart(1990)
S.newplan(-20,100)

S.newgroupstart(2070)
S.newplan(0,100)

S.newgroupstart(2150)
S.newplan(50,100,'26_')
S.newplan(140,100,'27_')
S.newplan(0,200)
S.newplan(200,200)


CMD=[]
CMD += ROOF(S[1]) + ROOF(S[2]) + ROOF(S[3]) + ROOF(S[4]) + ROOF(S[5]) + ROOF(S[6]) \
+ ROOF(S[7]) + ROOF(S[8]) + roof2(S[8]) + ROOF(S[9]) \
      + roof2(S[9]) + ROOF(S[10]) + roof2(S[10]) + ROOF(S[11]) + roof2(S[11]) + ring(S[0])
CMD += firework2(S[12], [378.5, 7,192.5]) + firework2(S[13], [378.5, 7, 187.5]) + firework2(S[14], [378.5, 7,182.5]) \
     + firework2(S[15], [378.5, 7, 177.5]) + firework2(S[16], [378.5, 12, 172.5]) + firework2(S[17], [378.5, 14, 167.5]) \
     + firework2(S[18], [378.5, 19, 162.5]) + firework2(S[19], [378.5, 20, 157.5]) + firework2(S[13], [378.5, 7, 187.5]) \
     + firework2(S[20],[378.5, 23, 152.5]) + firework3(S[21], [430, 15, 90])
CMD += Firework(S[22],False)+Firework(S[23],False)
CMD +=firework4(S['22_'],1)+firework4(S['23_'],2)
CMD +=String1(S[24])+firework2(S[24], [393, 66,130],offset=0.75,s=0.25)
CMD +=String2(S[25])+picture(S[25],30,[370.5,110,130])
CMD += Firework(S[26])+Firework(S[27])
CMD +=firework4(S['26_'],1)+firework4(S['27_'],2)

ani_func.add_cmd(CMD)
ani_func.save_seq_file('firework_newyear', namespace='mcae')

copy2there('../Release', r'F:\mc\mc\.minecraft\versions\1.18.2-Fabric\saves\sjtu\datapacks\fireworks\data\mcae\functions')

# minecraft:entity.firework_rocket.large_blast_far
# minecraft:entity.firework_rocket.twinkle_far
# /playsound minecraft:entity.firework_rocket.twinkle_far ambient @a ~-500 ~ ~ 999

