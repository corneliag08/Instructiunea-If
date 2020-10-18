nrg=int(input("Numarul de gaini :"))
nrb=int(input("Numarul total de boabe :"))
nrbg=nrb//nrg
nrbc=nrb-(nrg*nrbg)
if (nrbg>nrbc):
    print("Gainile primesc mai multe boabe cu ",nrbg-nrbc,"boabe")
if (nrbc>nrbg):
    print("Curcanul primeste mai multe boabe cu " , nrbc-nrbg,"boabe")
else:
    print("Gainile si curcanul primesc acelasi numar de boabe")    