modal = 100000000
for x in range(1,9):
    if(x>=1 and x<=2):
        a = modal*0
        print("Laba Bulan Ke-",x," : ",a)
    if(x>=3 and x<=4):
        b = modal*0.1
        print("Laba Bulan Ke-",x," : ",b)
    if(x>=5 and x<=7):
        c = modal*0.5
        print("Laba Bulan Ke-",x," : ",c)
    if(x==8):
        d = modal*0.2
        print("Laba Bulan Ke-",x," : ",d)
total=a+a+b+b+c+c+c+d
print("Total : ",total)