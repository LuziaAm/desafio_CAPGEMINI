
from Classes.diferenca import Diferenca

n = [1, 5, 3, 4, 2]
x = 2

resposta = 3

def test_diferenca():
    assert Diferenca.diferenca(n, x) == resposta