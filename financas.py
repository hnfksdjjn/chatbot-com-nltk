def calcular_saldo(capital, gastos):
    """
    Função que calcula o saldo restante após os gastos.
    :param capital: O valor do salário ou capital inicial.
    :param gastos: Lista com os valores das despesas.
    :return: Tupla com o saldo restante e o total de gastos.
    """
    total_gastos = sum(gastos)
    saldo_restante = capital - total_gastos
    return saldo_restante, total_gastos

