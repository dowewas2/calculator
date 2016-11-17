#defines variables and function




var('y,x,x_0,x_1,x_2,h_1,h_2,f_0,f_1,f_2,d,dd,ddd')

# p(x) =((x-x_1)*(x-x_2)*(f_0))/((x_0-x_1)*(x_0-x_2))+((x-x_0)*(x-x_2)*(f_1))/((x_1-x_0)*(x_1-x_2))+((x-x_0)*(x-x_1)*(f_2))/((x_2-x_0)*(x_2-x_1))
w(x)=(x-x_0)*(x-x_1)*(x-x_2)
s = diff(w,x,1)
ss = diff(w,x,2)
p(x) = ddd*w(x) + d*s+ dd/6*s + d/6*ss

#example
#p(x_1) or p(3)

print(diff(p,x,1))