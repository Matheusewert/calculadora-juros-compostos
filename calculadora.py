valor = float(input("Valor inicial (R$): "))
aporte = float(input("Aporte mensal (R$): "))
taxa = float(input("Taxa de juros ao mês (%): ")) / 100
meses = int(input("Prazo (meses): "))

saldo = valor
for mes in range(meses):
    saldo = saldo * (1 + taxa) + aporte

investido = valor + aporte * meses
print(f"Total investido: R$ {investido:.2f}")
print(f"Saldo final: R$ {saldo:.2f}")
print(f"Juros ganhos: R$ {saldo - investido:.2f}")
