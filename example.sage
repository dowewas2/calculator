

#Solve a system of equations

A = matrix([
	[0,0,0,1,0,0,0,0],
	[8,4,2,1,0,0,0,0],
	[0,0,0,0,8,4,2,1],
	[0,0,0,0,27,9,3,1],
	[12,4,1,0,-12,-4,-1,0],
	[0,2,0,0,0,0,0,0],
	[0,0,0,0,18,2,0,0],
	[12,2,0,0,-12,-2,0,0]])

b = vector([0,1,1,0,0,0,0,0])

A.solve_right(b)

#Integrates a function with respect to x
integrate(2*cos(x/2),x)
#Differentiate a function with respct to x
derivative(sin(x/2),x)


print "hello world"
print 2^3

# Calculates A
def fun_one(P,r,t):
    A = P + t + r^2
    return A
    
# Calculates amount invested
def fun_two(P,r,t,n):
    A = t*(1+r/n)^(n*t^2)
    return A
# Calculates amount invested (contin)
# Calculates amount invested (contin)
def fun_three(P,r,t):
    A = P*e^(r*t)
    return 2*A*A