# Değişken tanımlama örnekelri
x = 5
y = "Merhaba, Dünya"
z = True

# VERİ TİPLERİ
# 1. Tam sayılar (integer)
x = 15
y = -15
z = 0

# 2. Ondalıklı sayılar (floats)
x = 3.14
y = -2.25
z = 1.0

# 3. metin (string)
selam = "Merhaba!"
ad = "Ahmet"
mesaj = selam + " " + ad
print(mesaj)

# 4. Boolean (True veya False)
x = True
y = False

a = 7
b = 3
print(a > b)# True
print(a == b)# False

# 5. Listeler (list)
meyveler = ["elma","armut","çilek","portakal"]
print(meyveler)
print(len(meyveler))
print(meyveler[0]) # ilk eleman
print(meyveler[3]) # son eleman ama sayi her zaman bilinmez
print(meyveler[len(meyveler)-1])

# 6. Demetler (turple)
sayilar = (1,2,3)
print(sayilar)
print(len(sayilar))
print(sayilar[0]) # ilk eleman
print(sayilar[-1])
# sayilar[1] = 4 -> tuple icindeki elemanlar degismez
print(sayilar)

# 7.sayilar (dictionary -> dict
# anahtar: deger
sozluk = {
    "marka": "Apple",
    "model": "Macbook pro",
    "yil": 2021,
}
print(sozluk)
print(sozluk["marka"])
print(sozluk.get("marka"))
print(sozluk.get("fiyat",0.00))
sozluk["fiyat"] = 20000.0
print(sozluk)
print(sozluk.get("fiyat",0.0))

#8. kumeler (set)
kume = {1,2,3,4,5,}
print(kume)
kume.add(6)
print(kume)
kume.add(6)
print(kume)
kume.add("Ahmet")
print(kume)
kume.remove("Ahmet")
print(kume)
kume.update([6,7,"Ahmet","Kerem","Ahmet"])
print(kume)



#VERI TIPI DONUSUMLERI
sayi1 = input("1.sayiyi yazin:")
sayi2 = input("2.sayiyi yazin:")
toplam = sayi1 + sayi2 #string degerleri birlestirdi
print(type(sayi1),type(sayi2))
sayi1 = int (sayi1)
sayi2 = int (sayi2)
print(type(sayi1), type(sayi2))
print(sayi1 + sayi2)

x = 1
y = 1.8
liste = ["Turkce","Matematik","Fen","turkce"]
print(float(x))
print(int(y))
print(x + y)
print(bool(x)) #True
print(bool(y)) #True
print(bool(0)) #False
print(bool(o.8)) #True
print(bool(-1)) #True
print(bool(int(0.8))) #False
print(int(True))
print(int(False))
print(type(str(x)))
print(type(str(y)))
print(tuple(liste))
print(set(liste))