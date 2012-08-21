import numpy as np
import scipy.misc.pilutil as smp

def blackborder(x, y, size):
    if x == 0 or x == 1 or x == 2 or x == size - 1 or x == size - 2 or x == size - 3:
        r = 0
        g = 0
        b = 0
        return r, g, b
    elif y == 0 or y == 1 or y == 2 or y == size - 1 or y == size - 2 or y == size - 3:
        r = 0
        g = 0
        b = 0
        return r, g, b

def blacklines(x, y, size):
    if x == y or x + 1 == y or x == y + 1 or x + y == size or x + y + 1 == size or x + y == size + 1:
        r = 0
        g = 0
        b = 0
        return r, g ,b
    
def toptriangle(x,y,size):
    if x < y and x + y < size:
        r = y / (size/float(255))
        g = x * y / (size/float(255))**2
        b = (size - y) / (size/float(255))
        return r, g, b

def bottomtriangle(x,y,size):
    if x > y and x + y > size:
        r = y / (size/float(255))
        g = x * y / (size/float(255))**2
        b = (size - y) / (size/float(255))
        return r, g ,b
    
def lefttriangle(x,y,size):
    if x < y and x + y > size:
        r = y / (size/float(255))
        g = x * y / (size/float(255))**2
        b = (size - y) / (size/float(255))
        return r, g ,b
        
def righttriangle(x,y,size):
    if x > y and x + y < size:
        r = y / (size/float(255))
        g = x * y / (size/float(255))**2
        b = (size - y) / (size/float(255))
        return r, g, b

def color(x, y, size):
#    r = (y - x) % size / (size/float(255))
#    g = x * y / (size/float(255))**2
#    b = (size - y) / (size/float(255))

    r = 0
    g = 0
    b = 0
    
    # Grid
    if x % 32 == 0 or y % 32 == 0:
        r = 255 - r
        g = 255 - g
        b = 255 - b
    
    pixel = [ r, g, b]
    return pixel

xsize = 512
ysize = 512

# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros( (xsize,ysize,3), dtype=np.uint8 )

for y in range(xsize):
    for x in range(ysize):
        data[x,y] = color(x,y, 512)

img = smp.toimage(data)       # Create a PIL image
img.show()                    # View in default viewer