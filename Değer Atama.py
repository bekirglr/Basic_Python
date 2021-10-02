a = 2 
b = a + 5

#a = a + 3

print(b)   #b=>7

#4. satırdaki fonksiyonu aktif hale getirdiğimizde "a= 5" görürüz. Bunun sebebi a'ya yeni değer atamamızdır. Peki 1.satır noldu? 1.satır, 4 satır devreye girdiğinde etkisini kaybediyor ve a'ya yeni değer atanıyor ve bundan sonraki a değerimiz 5 oluyor

a = 2 
b = a + 5
a = a + 3

print(a) 

#ÖRNEK
maasBekir = 3000
maasCelal = 5000 
vergi = 0.25

print(maasBekir - (maasBekir * vergi ))     # bekir maaşı
print(maasCelal - (maasCelal * vergi ))     # celal maaşı
