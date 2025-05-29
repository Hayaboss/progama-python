#a função na qal é calculado o saldo do salario 

def calcular_saldo(salario, gastos):
    total_gastos = 0
    for i in range(len(gastos)):  
        total_gastos += gastos[i][1]  

    saldo_restante = salario - total_gastos
    return total_gastos, saldo_restante