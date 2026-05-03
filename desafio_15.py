km = float(input('Quantos Km foram percorridos? '))
dias = int(input('Quantos dias foram percorridos? '))
valor = (dias * 60) + (km * 0.15)

print(f'O valor do aluguel ficou em R${valor:.2f}')