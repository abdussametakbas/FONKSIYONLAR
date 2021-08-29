def selamlama(isim="kullanıcı",mesaj="iyi Günler"):
    print(f'{mesaj} {isim}')

selamlama("Ali", "Günaydın")
selamlama("Ali", "İyi Günler")
selamlama("Ali")                       # herhangi birşey göndermessen fonksiyondaki standartı alır.
selamlama()

def usAlma(taban, us=2):
    return taban**us
sonuc= usAlma(2,3)
sonuc= usAlma(2)              #taban'ı tanımladıktan sonra bu ifadeyi girersen hata verir. üsü'de tanımlaman lazım



def toplam(a,b):
    return a+b
def cikarma(a,b):
    return a-b

def islem(a,b ):             #standart
    return toplam(a,b)
sonuc=islem(10,20)       

def islem(a,b,fn ):
    return fn(a,b)             
sonuc=islem(10,20,toplam)    #toplam veya cıkarma yı sonradan böyle ekleyebiliriz

def islem(a,b,fn=toplam ):
    return fn(a,b)             
sonuc=islem(10,20, cikarma)  #en başta toplam tanımlayıp sonradan değiştirme de yapabiliriz.


print(sonuc) 
