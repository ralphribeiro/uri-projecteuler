def converte_tempo(valor: int):
    h = (valor // 3600)
    m = (valor % 3600) // 60
    s = (valor % 3600) % 60

    retorno = f'{h}:{m}:{s}'
    return retorno
