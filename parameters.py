def selamla(isim):
    return "merhaba, " + isim

sonuc= selamla("ahmet")
sonuc= selamla("Yağmur")
print(sonuc)    

def toplam(a,b):
    return a+b
sonuc= toplam(10,20)
print(sonuc)

def yasHesapla(dogumYili):
    return 2021- dogumYili
sonuc=yasHesapla(2002)
print(sonuc)



def emekliligeKacYilKaldi(dogumYili,isim):
    yas= yasHesapla(dogumYili)
    KalanSure= 65 - yas

    if KalanSure>0:
        print(f'sayın {isim} , emekliliğe {KalanSure} yıl kaldı.')
    else:
        print(f'sayın {isim}, zaten {abs(KalanSure)} yıl önce emekli oldunuz. '    )      #abs( )  mutlak değeri alır.
emekliligeKacYilKaldi(1935,"Abdussamet")   
emekliligeKacYilKaldi(1980,"Aydın")   

# print(sonuc) 