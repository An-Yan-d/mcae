import os
import numpy as np


def read_animation_vertices(objFilePath):
    f=0
    with open(objFilePath) as file:
        points = []
        while 1:
            line = file.readline()
            if not line:
                break
            
            strs = line.split(" ")
            if strs[0] == "Frame":
                f=int(strs[1])-1
                points.append([])
            if strs[0] == "v":
                points[f].append((float(strs[1]), float(strs[2]), float(strs[3])))
    return points



if __name__=='__main__':
    croods=read_animation_vertices(r'F:\program\particles_MC\mcae-main\files\output.txt')
    print(croods)



