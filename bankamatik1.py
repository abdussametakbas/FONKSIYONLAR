# Bankamatik uygulaması

# bu uygulamada ana hesap ve ek hesap kullanılacaktır

SametHesap= {
    'ad':"Abdussamet",
    'HesapNo' : 1001,
    'KullanılabilirBakiye':8000,
    'EkHesapBakiye':2000
}
AydınHesap= {
    'ad':"Aydın",
    'HesapNo':1002,
    'KullanılabilirBakiye':3000,
    'EkHesapBakiye':1000
}
def paraCek(hesap, miktar):
    print(f"Merhaba, { hesap['ad']}")

    if miktar<=hesap['KullanılabilirBakiye']:
        hesap['KullanılabilirBakiye']-=miktar
        print(f'Paranızı alabilirsininiz. {miktar} TL ')
        bakiyeSorgula(hesap)
    else:
        toplam= hesap['KullanılabilirBakiye'] + hesap['EkHesapBakiye']
        if toplam>=miktar:
            ekHesapKullanimi=input('Kullanılabilir bakiyeniz yetersiz, ek hesap kullanmak istermisiniz (e/h): ')
            if ekHesapKullanimi=='e':
                ekHesapKullanilacakMiktar= miktar-hesap['KullanılabilirBakiye']
                hesap['KullanılabilirBakiye']=0
                hesap['EkHesapBakiye']-=ekHesapKullanilacakMiktar
                print(f'paranızı alabilirsiniz. {miktar} TL\n{ekHesapKullanilacakMiktar} TL ek hesaptan çekilmiştir, Bilginize')
                bakiyeSorgula(hesap)
            else:
                print('İşleminiz iptal edilmiştir. İyi Günler.')
                bakiyeSorgula(hesap)
        
        
        
        else:
            print('Üzgünüz, hesap bakiyeniz yetersiz!')
            bakiyeSorgula(hesap)









def bakiyeSorgula(hesap):
    print(f"Sayın {hesap['ad']}, {hesap['HesapNo']} nolu hesabının bakiyesi: {hesap['KullanılabilirBakiye']}\nek hesap limiti {hesap['EkHesapBakiye']}")

paraCek(SametHesap,9000)


