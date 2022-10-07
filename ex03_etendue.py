#!/usr/bin/python3

def etendue(tableau):
    ...

# pour validation, ne pas modifier
def test():
    print("Tests etendue...")
    assert etendue([1]) == 0
    assert etendue([5,4,3,2,1]) == 4
    assert etendue([0,4,3,2,1]) == 4
    assert etendue([1,4,3,2,1]) == 3
    assert etendue([-5,-4,-3,-2,-4]) == 3

    assert etendue([]) == 0
    assert etendue([1,1,1,1,1,1,1]) == 0
    assert etendue([-1, -1, -1, -1]) == 0
    print("Tous les tests sont OK !")

test()