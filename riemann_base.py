import math

def fnf(i):  
  return #here's go the function  
 
a = #start
b = #end
numberofsteps = #number of steps
deltax = (b - a) / numberofsteps
x = a # <- for the left, for the middle: + deltax / 2, for the right: + deltax
accumulation = 0

for x in range(0, numberofsteps):
  deltaS = fnf(x) * deltax  
  accumulation += deltaS  
  x += deltax  
  print(deltaS, accumulation)
