qtd = int(input("Digite a quantidade de números: \n >>"))
contador = 0
soma = 0
media = 0

while contador < qtd:

    numero = float(input("Digite o número: \n"))
    soma = soma + numero
    contador += 1
  
media = soma/qtd

print("Somatório = \n", soma)
print("Quantidade = \n", qtd)
print("Média = \n", '{:.2f}'.format(media))