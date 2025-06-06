"""
Módulo de testes para a função soma do módulo main.
"""

from main import soma

def test_soma():
    """
    Testa a função soma com diferentes entradas.
    """
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(1.5, 2.5) == 4.0
