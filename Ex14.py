def excesso(peso):
    excesso = max(peso - 50, 0)
    multa = int(excesso > 0) * 4 * excesso
    return multa

peso = float(input("Digite o peso do peixe: "))

multa_total = excesso(peso)

print("O valor a pagar é de: R$", multa_total)