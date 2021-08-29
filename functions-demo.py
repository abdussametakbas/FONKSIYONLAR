#  1 - kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız
def cogaltici(kelime, adet):
    i=1
    while i<=adet:
        print (kelime)
        i+=1
cogaltici("Bilgisayar",4)


#  2 - dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def alan_cevre(KısaKenar, UzunKenar):
    print(f'Alan : {KısaKenar*UzunKenar}\nÇevre : {2*(KısaKenar+UzunKenar)}')
alan_cevre(5,7)


#  3 - yazı tura uygulamasını fonksiyon kullanarak yapınız (random modülü).
def yazimiTurami(tahmin):
    import random
    sonuc=random.randint(1,2)
    if sonuc==1:
        sonuc="tura"
    else:
        sonuc="yazı"
    if tahmin==sonuc:
        return f"doğru bildiniz : {sonuc}"
    else:
        return f"yanlış bildiniz : {sonuc}"
print(yazimiTurami("tura"))
    

#  4 - kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
def asalBul(sayi1, sayi2):
    # asalMi=True
    for sayi in range(sayi1,sayi2+1):
        if sayi>1:
            for i in range(2, sayi):             #  ÖNEMLİ   ++
                if sayi%i==0:
                    break
            else:
                print(sayi)  
asalBul(10,20)                          



#  5 - kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınınz.
def tamBölenBul(sayi):
    tamBölenler=[]
    for i in range(1,sayi+1):
        
        if sayi%i==0:
            tamBölenler.append(i)

        else:
            pass
    print(tamBölenler)
tamBölenBul(10)        


