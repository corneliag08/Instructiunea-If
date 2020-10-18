a=int(input("Primul numar :"))
b=int(input("Al doilea numar :"))
c=int(input("Al treilea numar :"))
if ((a>=0) and (b>=0) and (c>=0)):
    if (b>c):
        print(b)
    else : 
        print (c)
else : 
    print (a+b)