# importando da pagina relatorio que seria a soma que dasayev fez
from relatorio import calcular_saldo

def solicitar_dados_usuario():
    # pede o nomee e quanto o usario ganha
    nome = input("Digite seu nome: ")
    salario = float(input("Digite seu salário mensal (R$): "))
    return nome, salario

def registrar_gastos():
    #guarda os gastos no arquivo gastos.txt
    gastos = []
    print("\nAgora, vamos registrar seus gastos mensais.")

    with open("gastos.txt", "a") as arquivo:  # Modo "a" para adicionar sem sobrescrever
        while True:
            categoria = str(input("Digite a categoria de gasto (ou 'sair' para encerrar): "))
            if categoria.lower() == "sair":
                break
            valor = float(input("Digite o valor gasto com a categoria informada acima R$:"))
            if valor<0:
                print("Valor invalido!")
                continue #o continue faz com q o programa iguinore oq ta abaixo dele e volte pra o inicio do while
            else:
                gastos.append((categoria, valor))
            # Salvando no arquivo
            arquivo.write(f"{categoria}, {valor:.2f}\n")

    return gastos

def exibir_relatorio(nome, salario, gastos, total_gastos, saldo_restante):
    #Exibe um relatório com os gastos e saldo restante.
    print("\n===== RELATÓRIO DE GASTOS MENSAIS =====")
    print("Nome:", nome)
    print(f"Salário: R$ {salario:.2f}")
    
    print("\nGastos por categoria:")
    for i, (categoria, valor) in enumerate(gastos):
        print(f"{i} - {categoria} - R$: {valor:.2f}")
    
    print(f"\nTotal de gastos: R$ {total_gastos:.2f}")
    print(f"Saldo restante: R$ {saldo_restante:.2f}")

    if saldo_restante < 0:
        print("\nAtenção: você gastou mais do que o seu salário!")
    else:
        print("\nParabéns! Você está controlando bem seus gastos.")

def main():
    """Função principal que orquestra o programa."""
    nome, salario = solicitar_dados_usuario()
    gastos = registrar_gastos()
    total_gastos, saldo_restante = calcular_saldo(salario, gastos)
    exibir_relatorio(nome, salario, gastos, total_gastos, saldo_restante)

# Execução do programa
if __name__ == "__main__":
    main()