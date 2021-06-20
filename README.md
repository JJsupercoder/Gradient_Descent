# Gradient_Descent
Calculate the minima of any convex f(x) using Gradient Descent method
Formula: xn+1 = xn - r*f'(xn)
where r = (xn - xn-1)/(f'(xn) - f'(xn-1))
xn is defined initially by user, xn-1 = (xn) - 1 

Do 'pip install sympy' in cmd
set accuracy > 0 and very close to 0 to get accurate minima
uses sympy to differentiate and Function_Derivative to plot function. 
Either keep Function_Derivative.py in same folder or comment out the line, FD.plot(func)
Good luck!
