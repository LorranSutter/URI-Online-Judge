salario = float(input())
reajuste = 0
percentual = 0

if salario <= 400:
	percentual = 15
elif salario <= 800:
	percentual = 12
elif salario <= 1200:
	percentual = 10
elif salario <= 2000:
	percentual = 7
else:
	percentual = 4

print("Novo salario: {:0.2f}".format(salario*(1+percentual/100)))
print("Reajuste ganho: {:0.2f}".format(salario*percentual/100))
print("Em percentual: {0} %".format(percentual))
