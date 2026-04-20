word = input('Digite algo: ')
wordType = type(word)
wordIsNumber = f"\n{word} é um número ? {word.isnumeric()}"
wordIsAlpha = f"\n{word} tem somente letras ? {word.isalpha()}"
wordIsUpper = f"\n{word} todas as letras são maiúscula ? {word.isupper()}"
wordIsLower = f"\n{word} todas as letras são minúscula ? {word.islower()}"
print(wordType,wordIsNumber, wordIsAlpha, wordIsUpper, wordIsLower)