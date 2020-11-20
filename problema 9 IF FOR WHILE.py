n=int(input("Dati un numar:"))
suma=0
for i in range(1,n):
    if n%i==0:
        suma+=i
print(suma)       
if suma==n:
    print("este un numar perfect")
else:
    print("nu este un numar perfect")
