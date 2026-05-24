from main import  add
def test_add_pos():
    assert  add(2, 3) == 5

def test_add_neg():
    assert add(-1, -4) == -5

def test_add_mmix():
    assert add(-2, 5) == 3
