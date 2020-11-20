m=eval(input("dati un numar:"))#numarator
n=eval(input("dati un numar:"))#numitor
o=eval(input("dati un numar:"))#numarator
p=eval(input("dati un numar:"))#numitor
e=(m*p+o*n)
f=n*p
g=m*o
from  fractions import Fraction
if n!=0 or p!=0:
    print("suma este =",Fraction(e,f))
    print("produsul este =",Fraction(g,f))
else:
    print("impartirea la 0 nu are sens")