import numpy as np
import scipy.misc.pilutil as smp
from random import *

##################################
# Geometry
##################################

def border(x, y, size, px=3):
    if (0 <= x and x <= px) or (size - 1 >= x and x >= (size - (1+px))) or (0 <= y and y <= px) or (size - 1 >= y and y >= (size - (1+px))):
        return True

def lines(x, y, size):
    if x == y or x + 1 == y or x == y + 1 or x + y == size or x + y + 1 == size or x + y == size + 1:
        return True
    
def toptriangle(x,y,size):
    if x < y and x + y < size:
        return True

def bottomtriangle(x,y,size):
    if x > y and x + y > size:
        return True

def lefttriangle(x,y,size):
    if x > y and x + y < size:
        return True

def righttriangle(x,y,size):
    if x < y and x + y > size:
        return True
    
def triangle(x,y,size):
    #TODO: fix right angle triangle
    if x > 2*y or 2*(size - y) < x or x < size/2:
        return True
    
def circle(x,y,size):
    if (x - size/2)**2 + (y - size/2)**2 <= (size/2)**2:
        return True

def grid(x,y,size):
    if x % 32 == 0 or y % 32 == 0:
        return True

##################################
# Color manipulation
##################################
    
def invert(p):
    inv = (255-p[0], 255-p[1], 255-p[2])
    return inv

def noise(p=None, color=False):
    if color:
        r = randrange(0,255)
        g = randrange(0,255)
        b = randrange(0,255)
        if p:
            return ((p[0]+r)/2,(p[1]+g)/2,(p[2]+b)/2)
        else:
            return (r,g,b)
    else:
        z = randrange(0,255)
        if p:
            return ((p[0]+z)/2,(p[1]+z)/2,(p[2]+z)/2)
        else:
            return(z,z,z)

def mix(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2,(p1[2]+p2[2])/2)

def blurr(data):
    newdata = data
    s = len(data)
    for y in range(xsize):
        for x in range(ysize):
            r = (data[x,y][0] + data[x-1,y][0] + data[(x+1)%s,y][0] + data[x,y-1][0] + data[x,(y+1)%s][0] + data[x-1,y-1][0] + data[x-1,(y+1)%s][0] + data[(x+1)%s,y-1][0] + data[(x+1)%s,(y+1)%s][0])/9
            g = (data[x,y][1] + data[x-1,y][1] + data[(x+1)%s,y][1] + data[x,y-1][1] + data[x,(y+1)%s][1] + data[x-1,y-1][1] + data[x-1,(y+1)%s][1] + data[(x+1)%s,y-1][1] + data[(x+1)%s,(y+1)%s][1])/9
            b = (data[x,y][2] + data[x-1,y][2] + data[(x+1)%s,y][2] + data[x,y-1][2] + data[x,(y+1)%s][2] + data[x-1,y-1][2] + data[x-1,(y+1)%s][2] + data[(x+1)%s,y-1][2] + data[(x+1)%s,(y+1)%s][2])/9
            newdata[x,y] = (r, g, b)
    
    return newdata
    
def pattern1(size):
    r = y + x / (size/255)**2
    g = y / (size/255)
    b = y / (size/255)
    return (r,g,b)

def pattern2(size):
    r = (y - x) % size / (size/255)
    g = x * y / (size/255)**2
    b = (size - y) / (size/255)
    return (r,g,b)

##################################
# Paint
##################################

def paint1(x, y, size):
    pixel = pattern1(size)
    
    if grid(x,y,size):
        pixel = invert(pixel)
    
    if triangle(x,y,size):
        pixel = pattern1(size)
        
    if circle(x,y,size):
        pixel = invert(pixel)
    
    if bottomtriangle(x,y,size):
        pixel = invert(pixel)
        
    pixel = mix(pixel,pattern2(size))
    
    return pixel

def paint2(x, y, size):
    pixel = invert(data[x,y])
    return pixel

if __name__ == '__main__':
    xsize = 2048
    ysize = 2048
    
    # Create a 1024x1024x3 array of 8 bit unsigned integers
    data = np.zeros( (xsize,ysize,3), dtype=np.uint8 )
    
    for y in range(xsize):
        for x in range(ysize):
            data[x,y] = paint1(x,y, 1024)
    
    img = smp.toimage(data)       # Create a PIL image
    img.show()                    # View in default viewer