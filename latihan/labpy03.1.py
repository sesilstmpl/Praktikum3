print("Program Bilangan Acak yang Lebih dari 0.5")

import random
n = int(input("Masukan jumlah N = "))
a = 0
for c in range (n):
    a+=1
    b = random.uniform(.0,.5)
    while 1:
        n = random.random()
        if n < 0.5:
            break
    print('Data ke:',a,'==>', b)