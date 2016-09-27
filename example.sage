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
def fun_three(P,r,t):
    A = P*e^(r*t)
    return 2*A