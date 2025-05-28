
# A FUNÇÃO RETORNA DOIS VALORES nome e salario
def solicitar_dados_usuario():
    nome = input("Digite seu nome: ")
    salario = float(input("Digite seu salário mensal (R$): "))
    return nome, salario

#Função retorna a lista de gastos.
#Cada gasto é armazenado como uma tupla : Categoria, valor
def registrar_gastos():
    gastos = []
    print("\nAgora, vamos registrar seus gastos mensais.")
    while True:
        categoria = input("Digite a categoria de gasto (ou 'sair' para encerrar): ")
        if categoria.lower() == "sair":
            break
        valor = float(input("Digite o valor gasto com a categoria informada acima R$: "))
        gastos.append((categoria, valor))
    return gastos

#Função recebe a lista de gastos e calcula o total.
#sum() faz a soma total e o resultado é retornado.
def calcular_total_gastos(gastos):
    return sum(valor for _, valor in gastos)

#Função exibir_relatorio
def exibir_relatorio(nome, salario, gastos, total_gastos, saldo_restante):
    print("\n===== RELATÓRIO DE GASTOS MENSAIS =====")
    print("Nome:", nome)
    print("Salário: R$ %.2f" % salario)
    print("\nGastos por categoria:")
    for i, (categoria, valor) in enumerate(gastos):
        print(f"{i} - {categoria} - R$: {valor:.2f}")
    print("\nTotal de gastos: R$ %.2f" % total_gastos)
    print("Saldo restante: R$ %.2f" % saldo_restante)

    if saldo_restante < 0:
        print("\nAtenção: você gastou mais do que o seu salário!")
    else:
        print("\nParabéns! Você está controlando bem seus gastos.")
#Função principal que orquestra o programa
def main():
    nome, salario = solicitar_dados_usuario()
    gastos = registrar_gastos()
    total_gastos = calcular_total_gastos(gastos)
    saldo_restante = salario - total_gastos
    exibir_relatorio(nome, salario, gastos, total_gastos, saldo_restante)

# Execução do programa
if __name__ == "__main__":
    main()
