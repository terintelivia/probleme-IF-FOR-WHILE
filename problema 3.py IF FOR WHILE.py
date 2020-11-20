import math
m=int(input("Introduceti m : "))
n=int(input("Introduceti n: "))
if ((m>n)or(m==n)):
    print("Nu corespunde conditiei")
else:
    l=round(math.log(n,m))
    if (m**l==n):
        print(n,"este o putere a lui",m)
    else:
        print(n,"nu este o putere a lui",m)