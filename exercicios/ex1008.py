def calcula_salario(funcionario: str,
                    horas_trabalhadas: float,
                    valor_hora: float
                    ):
    salario = horas_trabalhadas * valor_hora
    return f'NUMBER = {funcionario} \nSALARY = U$ {salario:.2f}'
