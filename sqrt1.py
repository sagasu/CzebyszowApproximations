def sqrt1(x):
# returns sqrt(1+x) for x between -0.8 and +0.25
   return 1 + x/2 - x*x/8 + x*x*x/16

def sqrtapprox(u):
# valid for x between 0.2 to 5.0
   if (u >= 1.25):
      return sqrt1(u/4-1)*2
   else:
      return sqrt1(u-1)
