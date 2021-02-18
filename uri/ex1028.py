"""Exercício 1208."""
from typing import List
from math import gcd


class Ex1028():
    """Com as figurinhas em mãos, cada um tentava fazer uma troca com o amigo
    que estava mais perto seguindo a seguinte regra: cada um contava quantas
    figurinhas tinha. Em seguida, eles tinham que dividir as figurinhas de
    cada um em pilhas do mesmo tamanho, no maior tamanho que fosse possível
    para ambos. Então, cada um escolhia uma das pilhas de figurinhas do
    amigo para receber. Por exemplo, se Ricardo e Vicente fossem trocar as
    figurinhas e tivessem respectivamente 8 e 12 figuras, ambos dividiam
    todas as suas figuras em pilhas de 4 figuras (Ricardo teria 2 pilhas
    e Vicente teria 3 pilhas) e ambos escolhiam uma pilha do amigo para
    receber.
    """
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def tamanho_maximo_pilha(self) -> int:
        return gcd(self.x, self.y)
