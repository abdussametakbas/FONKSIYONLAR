from datetime import date


def toplam():
    return 10+20

a=toplam()    #return yapınca değişkene koyuyoruz fonk ' u
print(toplam())  # buda aynı
print(a)

sonuc= toplam() + 50
print(sonuc)
                        
                         # Yaş hesaplama
def simdiYil():
    import datetime
    return datetime.datetime.now().year

def yasHesapla():
    yas=int(input('doğum tarihiniz: '))
    return simdiYil()-yas
print(yasHesapla())    


def saat():
    import datetime
    return datetime.datetime.now().hour
def selamla():
    if saat()> 8 and saat()<13:
        return "Günaydın"
    else:
        return "İyi Günler"

print(selamla())           

