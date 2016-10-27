
f=open('current.py')
line=f.readlines()
a = line[0]
b = str(a)
currentloan = float(b)
print(currentloan)
f.close()

ff=open('previous.py')
lines=ff.readlines()
aa = lines[0]
bb = str(aa)
previousloan = float(bb)
print(previousloan)
ff.close()

# ff=open('previous.py')
# lines=ff.readlines()
# aa = lines[0]
# aa.split()
# previousloan = int(aa[0])
# print(previousloan)
# ff.close()



interest = currentloan-previousloan

print(interest)



h=open('dummy.py','w')
h.write(repr(currentloan))
h.close()