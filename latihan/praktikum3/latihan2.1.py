print("Program Bilangan Acak yang Lebih dari 0.5")

import random
n = int(input("Masukan jumlah N = "))
for a in range (n):
    while 1:
        n = random.random()
        if n < 0.5:
            break
    print (n)