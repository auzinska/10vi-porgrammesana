import math
a =float(input("Mala a:"))
b =float(input("Mala b:"))
c =float(input("Mala c:"))
if a>0. and b>0. and c>0.:
    if a<(b+c) and b<(a+c) and c<(a+b):
        print("var izveidot")
        pr = a + b + c
        pper = per/2.
        lauk = math.sqrt(per/2.*(pper-a)*(pper-b)*(pper-c))
        print("Perimetrs= {:.2f} Laukums= {:.2f}".format(per,lauk))33