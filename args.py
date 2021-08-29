# Değişken sayıda parametre : *args

def toplam(*args):    # yıldızlı (Şart) args (şart değil) veya başka bir şey yazarak istediğimiz kadar veri göndereceğimizi belirtiyoruz
    print(type(args))    #tuple
    print(args)
    sonuc=0
    for i in args:
        sonuc+=i
    return sonuc

print(toplam(10,20,30,150))