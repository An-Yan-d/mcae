import random

class schedule:
    def __init__(self,test=False):
        self.schedule= {}
        self.test=test
        self.group_st=0
        self.sign=0
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
    def newgroupstart(self,t):
        """
        大时间片段起始时间
        :return: None
        """
        self.group_st=t


class plan:
    def __init__(self, t, dt):
        """
        记录一个时间片段
        :param t: 起始时间
        :param dt: 时间跨度
        :param rnd: 是否随机
        :return: None
        """
        self.st = t
        self.dt = dt


    def time(self, st=0, et=1,rnd=False):
        if rnd:
            s=int(random.gauss(self.st + st * self.dt, 0.25))
            e=int(random.gauss(self.st + et * self.dt, 0.25))
            if s>e:
                s=e=int((e+s)/2)
            return s, e
        else:
            return int(self.st + st * self.dt), int(self.st + et * self.dt)