a=int(input("Primul numar :")) 
b=int(input("Al doilea numar :")) 
c=int(input("Al treilea numar :")) 
if ((a%2==0)and(b%2==0)and(c%2==0)): 
    print(a,"PAR") 
    print(b,"PAR") 
    print(c,"PAR") 
if ((a%2==0)and(b%2!=0)and(c%2==0)): 
    print(a,"PAR") 
    print(b,"IMPAR") 
    print(c,"PAR") 
if ((a%2==0)and(b%2==0)and(c%2!=0)): 
    print(a,"PAR") 
    print(b,"PAR") 
    print(c,"IMPAR") 
if ((a%2!=0)and(b%2!=0)and(c%2==0)): 
    print(a,"IMPAR") 
    print(b,"IMPAR") 
    print(c,"PAR")   
if ((a%2!=0)and(b%2==0)and(c%2==0)): 
    print(a,"IMPAR") 
    print(b,"PAR") 
    print(c,"PAR") 
if ((a%2==0)and(b%2!=0)and(c%2!=0)): 
    print(a,"PAR") 
    print(b,"IMPAR") 
    print(c,"IMPAR")
if ((a%2!=0)and(b%2==0)and(c%2!=0)): 
    print(a,"IMPAR") 
    print(b,"PAR") 
    print(c,"IMPAR") 
if ((a%2!=0)and(b%2!=0)and(c%2!=0)): 
    print(a,"IMPAR") 
    print(b,"IMPAR") 
    print(c,"IMPAR") 