a=int(input("dati numarul primei lature:"))
b=int(input("dati numarul celei de a doua latura:"))
c=int(input("dati numarul celei de a treia latura:"))
if(a+b>c)and(a+c>b)and(b+c>a):
    print("se formeaza triunghi cu asa laturi")
if((a!=b)and(a!=c)and(b!=c)):
    print("se formeaza un triunghi de tip scalen")
elif((a==b)and(a==c)and(b==c)):
    print("se formeaza un triunghi  de tip echilateral")
else:
    print("se fomeaza un triunghi de tip isoscel")
else:
    print("nu se formeaza triunghi cu astfel de laturi")