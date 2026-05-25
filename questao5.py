temperatura = float(input("Digite a temperatura da caldeira: "))

if temperatura < 100:
    print("Baixa")
elif temperatura <= 150:
    print("Normal")
else:
    print("Alerta: Temperatura Alta")