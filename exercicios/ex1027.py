import matplotlib.pyplot as plt

def encontra_pontos(txt: str) -> str:
    lista = txt.split('\n')
    n = 0
    x = []
    y = []
    y_medio = 0
    for l in lista:
        if ' ' in l:
            X, Y = l.split(' ')
            x.append(int(X))
            y.append(int(Y))
            y_medio += int(Y)
            plt.scatter(x, y)
        else:
            n = int(l)

    y_medio /= n
    
    y_medio = 0
    plt.plot([x[0], x[-1]], [y_medio, y_medio])

    contador = 0

    for i in range(len(y)):
        if (y_medio - 1) <= y[i] <= (y_medio + 1):
            if (y[i - 1] != y[i]):
                contador += 1
                plt.scatter(x[i], y[i], c='r')


    plt.show()

    return str(contador)


chamada = '10\n0 1\n1 0\n1 -1\n2 -2\n3 1\n3 -1\n3 -2\n4 1\n4 -1\n5 -1'
chamada2 = '10\n0 2\n2 0\n1 -1\n2 -2\n3 1\n3 -1\n3 -2\n4 1\n4 -1\n5 -1'

print(encontra_pontos(chamada))
# print(encontra_pontos(chamada2))
