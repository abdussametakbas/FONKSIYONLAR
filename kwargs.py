def displayUser(**kwargs):
    print(type(kwargs))        # <class 'dict'> kwargs'lar dictionary tutar.
    print(kwargs)              # {}

displayUser(username="sametakbas",email="akbas_samet_49@hotmail.com")    


def displayUser(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')
    

displayUser(username="sametakbas",email="akbas_samet_49@hotmail.com")    
