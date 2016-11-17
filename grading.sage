#Integrates a function with respect to x
var('x')

a = integrate(arctan(x)/(x^2+1),x,0,infinity)

b = integrate(ln(abs(x)),x,-1,1)

c = integrate(ln(x)/(e^x),x,2,infinity)

#Differentiate a function with respct to x

derivative(sin(x/2),x)


print(a)
print(b)
print(c)