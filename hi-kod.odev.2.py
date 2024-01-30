
#1
maas=int(input("Lutfen maasinizi giriniz:"))
if maas<=10000:
    yeni_maas = maas- maas*0.05
    print(yeni_maas)
elif maas<=25000:
    yeni_maas = maas- maas*0.1
    print(yeni_maas)
elif maas<=45000:
    yeni_maas = maas- maas*0.25
    print(yeni_maas)
else:
    yeni_maas = maas - maas*0.3
    print(yeni_maas)

#2

kullanici_adi=input("Lutfen bir kullanici adi giriniz:")
sifre=input("Lutfen bir sifre belirleyiniz:")
if len(sifre)>=6:
    print("Sifreniz olusturuldu")
else:
    print("En az 6 haneli yeni bir sifre olusturunuz")

#3

kullanici_adi=input("Lutfen bir kullanici adi giriniz:")
sifre=input("Lutfen bir sifre belirleyiniz:")
while len(sifre)<=5 or len(sifre)>10:
    print("Lutfen en az 5,en cok 10 haneli bir sifre giriniz:")
    sifre = input("Lutfen bir sifre belirleyiniz:")
print("Hesabınız olusturuldu.")


#4

dogru_sifre= "python123"
kullanici_adi=input("Lutfen kullanici adinizi giriniz:")
sifre=input("Lutfen sifrenizi giriniz:")
if sifre==dogru_sifre:
    print("Giris yapildi.")
else:
    print("Yanlis sifre girildi!")
    deneme_hakki=3
while deneme_hakki>=1 and sifre!=dogru_sifre:
    deneme_hakki-=1
    if deneme_hakki==0:
        print("Deneme hakkiniz kalmadi!")
    else:
        print("Yeniden deneyiniz.")
