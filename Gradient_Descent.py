import Function_Derivative as FD
from sympy import *

x,y = symbols('x y')
func = input("Enter f(x) to find local minima ")
f = lambda k: sympify(func.replace('x',str(k))).evalf()
FD.plot(func)

accuracy = 1e-10 #set accuracy as precise as you want the minima
df = lambda k: sympify(str(diff(eval(func),x)).replace('x',str(k))).evalf()

i1 = int(input("Enter an initial value of x "))
i0 = i1 - 1

while (abs(df(i1))>=accuracy):
    r = (i1-i0)/(df(i1)-df(i0))
    i1 = i0 - r*df(i0)

print("The estimated minima is",i1)
        
 
