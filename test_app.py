from main import soma

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(1.5, 2.5) == 4.0
