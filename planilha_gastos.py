# importando da pagina relatorio que seria a soma que dasayev fez
from relatorio import calcular_saldo
# Solicita os dados do usuário
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário mensal (R$): "))

# Lista para armazenar os gastos
gastos = []

# Inserção dos gastos
print("\nAgora, vamos registrar seus gastos mensais.")
with open("gastos.txt", "a") as arquivo:  # Modo "a" para adicionar sem sobrescrever
    while True:
        print("Gastos por categoria:")
        print("-------------------------")
        for i in range(len(gastos)):
            print(i, "-", gastos[i][0], "- R$: %.2f" % gastos[i][1])
        print("-------------------------")
        categoria = str(input("Digite a categoria de gasto ('r' para remover um item da Lista de gastos ou 'sair' para encerrar): "))
        if categoria.lower() == "sair":
            break
        elif categoria.lower() == "r":
            x=int(input("Informe o códugo do item da Lista a ser removido:"))
            print()
            if (x+1) <= len(gastos):
                gastos.pop(x)
                continue
            else:
                print()
                print("O item", x, "não está na Lista")
                print()
                continue
        valor = float(input("Digite o valor gasto com a categoria informada acima R$:"))
        if valor<0:
            print()
            print("Valor invalido!")
            print()
            continue #o continue faz com q o programa ignora oq ta abaixo dele e volte pra o inicio do while
        else:
            gastos.append((categoria, valor))
            # Salvando no arquivo
        arquivo.write(f"{categoria}, {valor:.2f}\n")
        arquivo.close

# Calcular totais
total_gastos, saldo_restante = calcular_saldo(salario, gastos)

# Exibir o relatório no terminal
print("\n===== RELATÓRIO DE GASTOS MENSAIS =====")
print("Nome:", nome)
print("Salário: R$ %.2f" % salario)
print()
print("Gastos por categoria:")
print("-------------------------")
for i in range(len(gastos)):
        print(i, "-", gastos[i][0], "- R$: %.2f" % gastos[i][1])
print("-------------------------")
print("Total de gastos: R$ %.2f" % total_gastos)
print("Saldo restante: R$ %.2f" % saldo_restante)

if saldo_restante < 0:
    print("Atenção: você gastou mais do que o seu salário!")
else:
    print("Parabéns! Você está controlando bem seus gastos.")