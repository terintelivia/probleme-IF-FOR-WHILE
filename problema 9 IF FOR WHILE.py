"
Un număr natural se numește număr perfect dacă este egal cu suma divizorilor lui, în afară de el însuși. De exemplu, 6 este număr perfect ,
deoarece 6=1+2+3. Să se afle numerele perfecte mai mici decât numărul natural dat n."
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
