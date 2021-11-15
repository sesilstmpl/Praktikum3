bilangan_pertama = int(input("Masukkan Bilangan Pertama = "))
bilangan_kedua = int(input("Masukkan Bilangan Kedua = "))
bilangan_ketiga = int(input("Masukkan Bilangan Ketiga = "))

if bilangan_pertama > bilangan_kedua and bilangan_pertama > bilangan_ketiga: 
    print("Bilangan yang terbesar adalah bilangan pertama, yaitu    ",bilangan_pertama)

elif bilangan_kedua > bilangan_pertama and bilangan_kedua > bilangan_ketiga:
    print("Bilangan yang terbesar adalah bilangan kedua, yaitu",bilangan_kedua)

else :
    print("Bilangan yang terbesar adalah bilangan ketiga, yaitu",bilangan_ketiga)