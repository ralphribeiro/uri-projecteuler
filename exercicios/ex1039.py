def calcula_raio(arg: str):
    instancias = arg.split('\n')
    instancias.remove('')

    retorno = str()
    
    for i in instancias:
        n = [int(x) for x in i.split(' ')]
        r1, x1, y1, r2, x2, y2 = n

        d_1_2 = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

        if r1 > d_1_2 and r1 > r2:
            retorno += 'RICO\n'
        else:
            retorno += 'MORTO\n'

    return retorno
      