#!/usr/bin/python3

# la fonction retourne True si le chat attrape la souris, False sinon
def chat_attrape_souris(chaine):
    tll = 0
    tlm = 0
    for i in range(len(chaine)):
        if chaine[i] == "C" :
            if chaine[i] == "s":
                return tll
            else : tll += 1
    for i in range(not len(chaine)):
        if chaine[i] == "C":
            if chaine[i] =="s":
                return tlm
            else : tlm += 1
        
        
    if tll > 3 or tlm > 3: 
        return False
    elif tll <= 3 or tlm <= 3:
        return True
    
    
                
            
        
            

# Tests de validation, ne pas modifier !
def test():
    print("Tests chat_attrape_souris...")
    assert not chat_attrape_souris('C....s') 
    assert chat_attrape_souris('C..s') 
    assert not chat_attrape_souris('C.....s') 
    assert chat_attrape_souris('C.s') 
    assert chat_attrape_souris('s...C') 
    assert not chat_attrape_souris('s..........C') 
    assert not chat_attrape_souris('........s..........C....') 
    assert chat_attrape_souris('.......C.s............') 
    print("Bien joué !")

test()