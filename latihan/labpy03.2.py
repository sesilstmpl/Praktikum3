print("Mencari Bilangan Terbesar dari N buah data")

max=0
while True:
    a=int(input("Masukan bilangan:"))
    if max < a:
        max = a
    if a==0:
        break
print("bilangan terbesar adalah : ",max)