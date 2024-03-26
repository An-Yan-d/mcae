"""
用于处理大型粒子项目的时间线安排
"""

import random

class schedule:
    def __init__(self,test=False):
        self.schedule= {}
        self.test=test
        self.group_st=0
        self.sign=0

    def istest(self):
        return not self.test

    def newplan(self,t, dt, sign=''):
        """
        记录一个时间片段
        :param t: 起始时间
        :param dt: 时间跨度
        :param sign: 该时间片段标号
        :return: None
        """
        if not sign:
            sign = self.sign
            self.sign+=1
        self.schedule[str(sign)]=plan(t+self.group_st, dt)

    def __getitem__(self, item):
        return self.schedule[str(item)]
    def setnewgroupstart(self,t):
        """
        大时间片段起始时间
        :return: None
        """
        self.group_st=t

    def show(self):
        pass



class plan:
    def __init__(self, t, dt):
        """
        记录一个时间片段
        :param t: 起始时间
        :param dt: 时间跨度
        """
        self.st = t
        self.dt = dt
        self.sign = 0
        self.subplans={}


    def time(self,rnd=False,sigma=0.25,offset=0):
        """
        返回游戏时间
        :param st: 起始plan相对起始时间的百分比/绝对偏移量
        :param et: 结束plan相对起始时间的百分比/绝对偏移量
        :param rnd: 是否随机
        :param sigma: 方差
        :return: 起始游戏时间，结束游戏时间
        """

        if rnd:
            s=int(random.gauss(self.st , sigma))
            e=int(random.gauss(self.st + self.dt, sigma))
            if s>e:
                s=e=int((e+s)/2)
            return s, e
        else:
            return int(self.st)+offset, int(self.st + self.dt)+offset

    def timelist(self):
        return range(int(self.st),self.st + self.dt)

    def subplan(self,st, dt, sign=''):
        """

        :param st: 从plan的起始时间开始算subplan的起始时间
        :param dt: subplan的持续时间
        :param sign:
        :return:
        """
        if not sign:
            sign = self.sign
            self.sign+=1
        if st+dt<=self.dt:
            self.subplans[str(sign)]=plan(st+self.st, dt)
            return self.subplans[str(sign)]
        else:
            print('Task creation fails: The subplan end time is later than the plan end time')
    def __getitem__(self, item):
        return self.subplans[str(item)]

    def getduration(self):
        return self.dt