area = float(input("Metros quadrados a pintar: "))

cobertura_lata = 18 * 3
preco_lata = 80

latas_necessaria = (area + cobertura_lata - 1) // cobertura_lata

preco_total = latas_necessaria * preco_lata

print(f"Você precisara de: {latas_necessaria} latas de tinta")
print(f"Preço: {preco_total} reais")
