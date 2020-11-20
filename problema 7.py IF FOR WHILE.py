n=int(input("Introdu un număr: "))
suma1=1
suma2=1
a=0
for i in range(1,n+1):
    suma1=suma1*2+i
print("la",n,"ani","Mihai va primi",suma1,"$")
while suma2<=100:
    a+=1
    suma2=suma2*2+a
print("la",n,"ani","Mihai va primi mai mult de 100$")
