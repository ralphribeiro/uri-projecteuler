from itertools import count


def chamadas_recursivas(n: int) -> str:
    """Obtem o número de chamadas recursivas Fibonacci.

    Args:
        numero (int): número a ser processado

    Returns:
        str: retorna uma string com o resultado
    """
    c = count(start=0, step=1)

    def fibonacci(n):
        next(c)
        if n <= 1:
            return n
        else:            
            return fibonacci(n-1) + fibonacci(n-2)

    r = fibonacci(n)

    return(f'fib({n}) = {next(c)-1} calls = {r}')
