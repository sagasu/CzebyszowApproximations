import matplotlib.pyplot as plt
from scipy import interpolate, linspace

def cauchy(x):
    return (1 + x**2) ** -1

n = 16
x = linspace(-5, 5, n)

y = cauchy(x)
f = interpolate.BarycentricInterpolator(x, y)

newx = linspace(-5,5,200)
newy = f(newx)

plt.plot(x, y , 'o', newx, newy, '-')
plt.show()
