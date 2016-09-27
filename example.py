print "hello world"
print 2^3

# Calculates A
def fun_one(P,r,t):
    A = P + r + t
    return A
    
# Calculates amount invested
def fun_two(P,r,t,n):
    A = P*(1+r/n)^(n*t)
    return A
    
# Calculates amount invested (contin)
def fun_three(P,r,t):
    A = P*e^(r*t)
    return 2*A