# solves for x
def mysolve(f):
	var('x')
	return solve(f,x)

# plots a function

def myplot(f, a, b):
	var( 'x' )
	g = Graphics()
	g += plot(f, (x, a, b))	
	return g.show( )

def myplot2(f, g, a, b):
	var( 'x' )
	g = Graphics()
	g += plot(f, (x, a, b))	
	g += plot((1-x^2)^(-1/2), (x, -10, 10))
	return g.show( )




# computes the numerical value of an expression
def myapp(a):							
	return a.numerical_approx()



# limit for the left and right
def myleftlimit(f, a):
	var('x')
	return f.limit(x=a,dir='-')
def myrightlimit(f, a):
	var('x')
	return f.limit(x=a,dir='+')
def mylimit(f, a):
	var( 'x' )
	return f.limit( x=a )

# Solve a system of equations
def mysyeq(A,b ):
	return A.solve_right( b )
	

# Integrates a function with respect to x
def myintbounds(f,a,b):
	var('x')
	return integrate(f, x,a,b)

# Integrates a function with respect to x with bounds
def myint(f):
	var('x')
	return integrate(f, x)	

# Differentiate a function with respct to x

def myderiv(f):
	var('x')
	return derivative( f,x )
