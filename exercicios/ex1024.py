def criptografa(txt: str) -> str:
    retorno = ''
    for c in txt:
        if c == ' ' or not c.isalpha():
            retorno += c
        else:
            retorno += chr(ord(c) + 3)

    retorno = retorno[::-1]

    aux = ''
    tamanho = len(retorno)
    for r in range(tamanho // 2, tamanho):
        aux += chr(ord(retorno[r]) - 1)

    retorno = retorno[:(tamanho // 2)] + aux

    return retorno
