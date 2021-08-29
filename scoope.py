#   global ve local 

x='Samet'                 #bu (global)dir fonkun içinde ayrı tanımlanırsa eğer karışmaz oraya
def test(name):
    x=name
                          # fonk'un içindeki sadece fonk'a özel (Local) 
    print(x)

print(x)          #Samet        
test("Aydın")     #Aydın



sayi=100
def degisim():
    global sayi
    print(sayi)
    sayi=50
    print(sayi)
degisim()               # **** burada global ile değişkeni fonk'a tanımlarsak dışarıda değişim yapar gibi oyanayabiliriz.
print(sayi) 
    
