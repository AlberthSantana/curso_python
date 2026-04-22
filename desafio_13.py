salario = float(input('Digite o salário do funcionário: '))
aumento = float(input('Digite o aumento: '))
salarioTotal = salario + ( salario * (aumento / 100))

print(f'O salário de R${salario:.2f} reais,será de R${salarioTotal:.2f}.')