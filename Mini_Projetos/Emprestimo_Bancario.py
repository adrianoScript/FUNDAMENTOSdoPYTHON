casa = float(input('Valor da casa R$: '))
salario = float(input('Salario do comprador: '))
anos = int(input('Anos de financiamento: '))
prestação = casa / (anos * 12)
minimo = salario * (30 / 100)

print(f"Para pagar uma casa de R${casa:.2f} em {anos}  anos ", end='')
print(f"a prestação será de R${prestação:.2f}")
print(f"Comparando tem que pagar {prestação:.2f} e o minimo é de {minimo:.2f}")

if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')