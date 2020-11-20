n=int(input("Introdu numărul: "))
if ((n<28)or(n>31)):
    print("nu sunt luni cu asa numar de zile")
elif n==28:
    print("februarie, daca nu e an bisect")
elif n==29:
    print("februarie, daca e an bisect")
elif n==30:
    print("aprilie,iunie,septembrie,noiembrie")
elif n==31:
     print("ianuarie,martie,mai,iulie,august,octombrie,decembrie")
   
