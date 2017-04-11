import math

def fnf(i):  
  return #here's go the function  
 
a = 1
b = 3
numberofsteps = 4
deltax = (b - a) / numberofsteps
x = a
accumulation = 0

for x in range(0, numberofsteps):
  deltaS = fnf(x) * deltax  
  accumulation += deltaS  
  x += deltax  
  print(deltaS, accumulation)
