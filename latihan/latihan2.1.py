print("Program Bilangan Acak yang Lebih dari 0.5")

from random import random
n = int(input("Masukan jumlah N = "))
for i in range (n):
    while 1:
        n = random()
        if n < 0.5:
            break
    print (n)