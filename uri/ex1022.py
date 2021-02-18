from fractions import Fraction

def calcula_expressao(expressao: str):
        N = []
        D = []
        c = 0
        lista = expressao.split(' ')
        operacao_meio = lista[3]
        for l in lista:
            if l in ['/'] and c != 3:
                N.append(lista[c - 1])
                D.append(lista[c + 1])
            c += 1

        f1 = Fraction(int(N[0]), int(D[0]))
        f2 = Fraction(int(N[1]), int(D[1]))

        if operacao_meio == '+':
            fr = f1 + f2
        elif operacao_meio == '-':
            fr = f1 - f2
        elif operacao_meio == '*':
            fr = f1 * f2
        else :
            fr = f1 / f2            

        return f'{fr.numerator}/{fr.denominator}'
