largura = float(input('Qual a largura da parede em metros: '))
altura = float(input('Qual a altura da parede em metros: '))
area = largura * altura
quantidadeDeTinta = area / 2

print(f'Esta parede tem {area} metros quadrados, gastara {quantidadeDeTinta} litros de tinta')