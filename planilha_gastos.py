# Solicita os dados do usuário
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário mensal (R$): "))

# Lista para armazenar os gastos
gastos = []

# Inserção dos gastos
print("\nAgora, vamos registrar seus gastos mensais.")
while True:
    categoria = str(input("Digite a categoria de gasto (ou 'sair' para encerrar): "))
    if categoria == "sair":
        break
    valor = float(input("Digite o valor gasto com a categoria informada acima R$:"))
    gastos.append((categoria, valor))

# Calcular totais
total_gastos=0
for i in range(len(gastos)):
        total_gastos += gastos[i][1]
saldo_restante = salario - total_gastos

# Exibir o relatório no terminal
print("\n===== RELATÓRIO DE GASTOS MENSAIS =====")
print("Nome:", nome)
print("Salário: R$ %.2f" % salario)
print()
print("Gastos por categoria:")
for i in range(len(gastos)):
            print(i, "-", gastos[i][0], "- R$: %.2f" % gastos[i][1])
print()
print("Total de gastos: R$ %.2f" % total_gastos)
print("Saldo restante: R$ %.2f" % saldo_restante)

if saldo_restante < 0:
    print("\n Atenção: você gastou mais do que o seu salário!")
else:
    print("\n Parabéns! Você está controlando bem seus gastos.")