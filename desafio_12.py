precoProduto = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))
valorTotal = precoProduto - ( precoProduto * (desconto / 100) )

print(f'O valor do produto de R${precoProduto}, ficara R${valorTotal}')