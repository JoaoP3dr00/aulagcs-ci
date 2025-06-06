import soma

def test_soma():
    assert main.soma(2, 3) == 5
    assert main.soma(-1, 1) == 0
    assert main.soma(0, 0) == 0
    assert main.soma(1.5, 2.5) == 4.0
