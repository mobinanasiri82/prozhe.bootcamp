import math
def calculate_delta(a,b,c):
    delta=(b**2)-(4*a*c)
    return delta
a=float(input("Andaze a ra vared konid:"))
b=float(input("Andaze b ra vared konid:"))
c=float(input("Andaze c ra vared konid:"))
delta=calculate_delta(a,b,c)
print("Andaze delta:" ,delta)
if delta>0:
    print("two roots exist:")
    print((-b+delta**0.5)/2*a)
    print((-b-delta**0.5)/2*a)
elif delta==0:
    print("one roots exist:")
    print((-b)/(2*a))
else :
    print("no real roots:")