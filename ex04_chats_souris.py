#!/usr/bin/python3

# la fonction retourne True si le chat attrape la souris, False sinon
def chat_attrape_souris(chaine):
    ...

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