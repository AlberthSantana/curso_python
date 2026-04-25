precoProduto = float(input('Digite o valor do produto: R$'))
desconto = int(input('Digite o valor do desconto %: '))
valorDesconto = precoProduto * desconto / 100
valorTotal = precoProduto - valorDesconto
print(f'O valor do produto de R${precoProduto:.2f}, com desconto de {desconto}%, ficara R${valorTotal:.2f}')