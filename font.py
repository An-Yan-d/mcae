from fontTools.ttLib import TTFont
import fontTools.varLib.plot as ftplt
import matplotlib.pyplot as plt
from scipy.special import comb
import points

utils=points.Utils()

class Font:
    def __init__(self, path):
        self.path = path
        self.font = TTFont(path)

    def font2coord(self, letter):
        z = [{'coord': itm[0], 'flag':itm[1]} for itm in zip(self.font['glyf'][self.font.getBestCmap(
        )[ord(letter)]].coordinates, self.font['glyf'][self.font.getBestCmap()[ord(letter)]].flags)]

        stpt = 0
        i = 0
        contour_order = 0
        coord = [[] for i in range(self.font['glyf'][self.font.getBestCmap()[
                                   ord(letter)]].numberOfContours)]
        for i in range(len(z)):
            coord[contour_order].append(z[i])
            if i in self.font['glyf'][self.font.getBestCmap()[ord(letter)]].endPtsOfContours:
                coord[contour_order].append(z[stpt])
                contour_order += 1
                stpt = i+1

        return coord

    def general_bezier(self, points_list, t, take):
        n = len(points_list)
        s = 0
        for i in range(n):
            s += points_list[i][take]*comb(n-1, i)*(1-t)**(n-i-1)*t**i
        return s

    def curve(self, points_list, step=10):
        n = int(((points_list[0][1]-points_list[-1][1])**2 +
                (points_list[0][0]-points_list[-1][0])**2)**0.5/step)
        if n == 0:
            n = 1
        dt = 1/n
        pl = []
        for i in range(n+1):
            pl.append([self.general_bezier(points_list, i*dt, 0),
                      self.general_bezier(points_list, i*dt, 1)])
        return pl

    def coord_refine(self, precoord):
        coord = []
        temp = []
        temp_line = []
        for part in precoord:
            for p in part:

                if p['flag'] == 1:
                    if temp:
                        if len(temp) != 1:
                            t = list(p['coord'])
                            temp.append(t)
                            temp_line += self.curve(temp)
                            temp = []
                            temp.append(t)
                        else:
                            temp_line.append(temp[0])
                            temp[0] = list(p['coord'])
                    else:
                        temp.append(list(p['coord']))
                elif p['flag'] == 0:
                    temp.append(list(p['coord']))

            temp = []
            coord.append(temp_line)
            temp_line = []
        return coord

    def is_in_poly(self, p, poly):
        """
        :param p: [x, y]
        :param poly: [[], [], [], [], ...]
        :return:
        """
        px, py = p
        is_in = False
        for i, corner in enumerate(poly):
            next_i = i + 1 if i + 1 < len(poly) else 0
            x1, y1 = corner
            x2, y2 = poly[next_i]
            if (x1 == px and y1 == py) or (x2 == px and y2 == py):  # if point is on vertex
                is_in = True
                break
            if min(y1, y2) < py <= max(y1, y2):  # find horizontal edges of polygon
                x = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
                if x == px:  # if point is on edge
                    is_in = True
                    break
                elif x > px:  # if point is on left-side of line
                    is_in = not is_in
        return is_in

    def point_generation(self, letter, step=5 , size=10,xrange=(0, 1024),yrange=(0,1024)):
        """
        :param letter:单个字，字符串类型

        """
        coord = self.coord_refine(self.font2coord(letter))
        points = []
        for x in range(*xrange, step):
            for y in range(*yrange, step):
                is_in = False

                for part in coord:
                    if self.is_in_poly([x, y], part):
                        is_in = not is_in
                if is_in:

                    points.append([x/1024*size, y/1024*size, 0])
        return points

    def string_generation(self, str, step=5 , size=10, distance=15):
        """
        :param str:字符串类型

        """
        print("--------------------")
        print("开始生成字符串")
        points=[]
        x=0
        for c in str:
            print(c)
            points+=utils.move(self.point_generation(c,step,size),x,0,0)
            x+=distance
        print("生成字符串完成")
        print("--------------------")
        return points

    def font_show_test(self, letter, process=True):
        """
        测试使用
        """
        fig = plt.figure()
        ax = plt.gca()
        if process:
            coord = self.coord_refine(self.font2coord(letter))
            for part in coord:
                for p in part:
                    ax.scatter(p[0], p[1], c='b', s=0.1)
        else:
            coord = self.font2coord(letter)
            for part in coord:
                for p in part:
                    if p['flag'] == 1:
                        c = 'b'
                    elif p['flag'] == 0:
                        c = 'r'
                    ax.scatter(p['coord'][0], p['coord'][1], c=c, s=0.1)

        ax.set_xlim(0, 1024)
        ax.set_ylim(-200, 924)
        plt.show()


if __name__=='__main__':
    f=Font(r'files/STFANGSO.TTF')
    f.font_show_test('暗',process=False)
    f.font_show_test('炎')
    p=f.point_generation('兴',step=10)
    from visualization import show_static
    show_static(p,size=0.1)
