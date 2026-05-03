import math
cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente =float(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f'A soma da hipotenusa {hipotenusa:.2f} ')