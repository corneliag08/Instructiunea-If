xa=int(input("Bile albe mici :"))
xr=int(input("Bile rosii mici :"))
xv=int(input("Bile verzi mici :")) 
ya=int(input("Bile albe mari :")) 
yr=int(input("Bile rosii mari :"))
yv=int(input("Bile verzi mari :"))
xt=xa+xr+xv
yt=ya+yr+yv
print("Numarul total de bile:",xt+yt,"bile")
if (xt>yt):
    print("Sunt ",xt,"bile mici")
if (yt>xt):
    print("Sunt",yt,"bile mari")
else:
    print("Bile mari si mici sunt egale")
if ((xa+ya>xr+yr) and (xa+ya>xv+yv)):
    print("Bile albe:",xa+ya)
if ((xr+yr>xa+ya) and (xr+yr>xv+yv)):
    print("Bile rosii:" ,xr+yr)
if ((xv+yv>xa+ya) and (xv+yv>xr+yr)):
    print("Bilr verzi",xv+yv)
if ((xr+yr==xa+ya)and(xr+yr>xv+yv)): 
    print("Bile albe si bile rosii sunt egale:",xa+ya) 
if ((xr+yr==xv+yv)and(xr+yr>xa+ya)): 
    print("Bile rosii si bile verzi sunt egale:",xr+yr) 
if ((xa+ya==xv+yv)and(xa+ya>xr+yr)): 
    print("Bile albe si bile rosii sunt egale:",xv+yv) 
else: 
    print("Bile albe,bile rosii si bile verzi sunt egale:",xa+ya)