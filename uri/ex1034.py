
def calcula_blocos(arg: str):
    parser = arg.split('\n')
    t = parser.pop(0)

    retorno = str()

    while len(parser) > 0:
        qtd = 0
        _, m = parser.pop(0).split()
        m = int(m)
        blocos = (int(x) for x in reversed(parser.pop(0).split()))

        b = next(blocos)
        while m > 0:
            if m < b: b = next(blocos)
            qtd += m // b
            m = m % b
            
        retorno += f'{qtd}\n'

    return retorno
