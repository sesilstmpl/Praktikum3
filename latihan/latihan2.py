def bilanganterbesar (bilangan_pertama,bilangan_kedua,bilangan_ketiga):
  if bilangan_pertama > bilangan_kedua and bilangan_kedua > bilangan_ketiga:
    return bilangan_pertama
  elif bilangan_kedua > bilangan_pertama and bilangan_pertama > bilangan_ketiga:
    return bilangan_kedua

  return bilangan_ketiga

def bilanganterkecil(bilangan_pertama, bilangan_kedua, bilangan_ketiga):
  if bilangan_pertama < bilangan_kedua and bilangan_pertama < bilangan_ketiga:
    return bilangan_pertama
  elif bilangan_kedua < bilangan_pertama and bilangan_kedua < bilangan_ketiga:
    return bilangan_kedua

  return bilangan_ketiga

def bilangantengah(bilangan_pertama, bilangan_kedua, bilangan_ketiga):
  if (bilangan_kedua > bilangan_pertama > bilangan_ketiga) or (bilangan_ketiga > bilangan_pertama > bilangan_kedua):
    return bilangan_pertama
  elif (bilangan_pertama > bilangan_kedua > bilangan_ketiga) or  (bilangan_ketiga > bilangan_kedua > bilangan_pertama):
    return bilangan_kedua
  
  return bilangan_ketiga

print("Program Pengurutan Data")
bilangan_pertama = int(input("Masukkan bilangan ke-1: "))
bilangan_kedua = int(input("Masukkan bilangan ke-2: "))
bilangan_ketiga = int(input("Masukkan bilangan ke-3: "))

A = bilanganterkecil(bilangan_pertama, bilangan_kedua, bilangan_ketiga)
B = bilangantengah(bilangan_pertama, bilangan_kedua, bilangan_ketiga)
C = bilanganterbesar(bilangan_pertama, bilangan_kedua, bilangan_ketiga)


print(f'Urutan bilangan: {A}, {B}, {C}')