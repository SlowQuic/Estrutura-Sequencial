hora_trabalhada = int(input("Horas trabalhas: "))
hora_paga = float(input("Pagamento por hora: "))

salario_bruto = hora_trabalhada * hora_paga

Imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
Sindicato = salario_bruto * 0.05
descontos = Imposto_de_renda + inss + Sindicato

salario_liquido = salario_bruto - descontos

print("Salario bruto: ", salario_bruto)
print("IR (11%) :", Imposto_de_renda)
print("INSS (8%) :", inss)
print("Sindicato (5%) :", Sindicato)
print("Salário Liquido : R$", salario_liquido)