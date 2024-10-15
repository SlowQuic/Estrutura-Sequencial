# Dados do produto
cobertura_por_litro = 6  # Cada litro cobre 6 m²
lata_litros = 18
lata_preco = 80
galao_litros = 3.6
galao_preco = 25
folga = 1.1  # Fator de folga de 10%

# Obtendo a área a ser pintada
area = float(input("Digite a área a ser pintada em metros quadrados: "))

# Calculando a quantidade de tinta necessária com folga
litros_necessarios = area / cobertura_por_litro * folga

# Calculando a quantidade de latas
latas_necessarias = (litros_necessarios + lata_litros - 1) // lata_litros
preco_latas = latas_necessarias * lata_preco

# Calculando a quantidade de galões
galoes_necessarios = (litros_necessarios + galao_litros - 1) // galao_litros
preco_galoes = galoes_necessarios * galao_preco

# Calculando a combinação de latas e galões
# Iniciando com o máximo de galões e ajustando as latas
latas_combinadas = 0
galoes_combinados = galoes_necessarios
while (latas_combinadas * lata_litros + galoes_combinados * galao_litros) < litros_necessarios:
    galoes_combinados -= 1
    latas_combinadas += 1
preco_combinado = latas_combinadas * lata_preco + galoes_combinados * galao_preco

# Imprimindo os resultados
print("-" * 30)
print("Resultados:")
print(f"Área a ser pintada: {area:.2f} m²")
print("-" * 30)
print(f"Utilizando apenas latas:")
print(f"   - Quantidade de latas: {latas_necessarias}")
print(f"   - Preço total: R$ {preco_latas:.2f}")
print("-" * 30)
print(f"Utilizando apenas galões:")
print(f"   - Quantidade de galões: {galoes_necessarios}")
print(f"   - Preço total: R$ {preco_galoes:.2f}")
print("-" * 30)
print(f"Utilizando latas e galões (menor desperdício):")
print(f"   - Quantidade de latas: {latas_combinadas}")
print(f"   - Quantidade de galões: {galoes_combinados}")
print(f"   - Preço total: R$ {preco_combinado:.2f}") 