# Kendisine gönderilen 2 sayıdan hangisi büyük bulan fonksiyonu yazınız.
def hangisiBüyük(sayi1,sayi2):
  if sayi1>sayi2:
    return f"{sayi1} ,{sayi2}'den büyüktür "
  elif sayi1<sayi2:
    return f"{sayi2} ,{sayi1}'den büyüktür "
  else:
    return f"sayılar eşittir"
sonuc= hangisiBüyük(10,20)
print(sonuc)


# Kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz.
def tekrarSayısı(kelime):
  return {letter: kelime.count(letter) for letter in kelime}
print(tekrarSayısı('flutter'))  



# Kendisine gönderilen list, command, position ve value bilgilerine göre liste üzerinde güncelleme yapınız.
   # [1,2,3], ("add, remove"), ("beginning | end"), value 
  # list_operation([1,2,3],"add","end","4") => [1,2,3,4]
  # list_operation([1,2,3],"remove","beginning") => [2,3]

def updat_list(liste, command, position, value=None):
  if command=="remove" and position=="end":
    liste.pop()
    return liste
  elif command=="remove" and position=="beginning":
    liste.pop(0)
    return liste
  elif command=="add" and position=="end":
    liste.append(value)
    return liste
  elif command=="add" and position=="beginning":
    liste.insert(0, value)
    return liste

print(updat_list([1,2,3,4],"add","end",15))



# Kendisine gönderilen renk isimlerinden içinde "blue" rengi varsa True döndüren fonksiyonu yazınız.
def kontrol(*args):
  for i in args:
    varmi=False
    if i=="blue":
      varmi=True
      print(varmi)
    else:
      print(varmi)
kontrol("red","blue","black","green")      
