salario = float(input("Digite o salário atual: "))
tempo = float(input("Digite o tempo de empresa em anos: "))

if tempo < 2:
    aumento = salario * 0.05
elif tempo <= 5:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print(f"Novo salário: R$ {novo_salario:.2f}")
