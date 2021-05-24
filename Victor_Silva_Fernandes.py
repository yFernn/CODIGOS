preco = float(input('Qual é o valor do produto?\n'))

qtd = int(input('Quantos desse produto você gostaria?\n'))

forma_de_pgt = int(input('Digite o código (1 a 4) da condição de pagamento de acordo com a tabela:\n'
                         '1 - À vista em dinheiro ou cheque, recebe 10% de desconto,\n'
                         '2 - À vista no cartão de crédito ou débito, recebe 5% de desconto,\n'
                         '3 - Em duas vezes, preço normal de etiqueta sem juros,\n'
                         '4 - Em três vezes, preço normal de etiqueta mais juros de 10%.\n'))

if forma_de_pgt == 1:
    print(f'Valor total da compra é de R$ {qtd * preco * 0.9:.2f}')
elif forma_de_pgt == 2:
    print(f'Valor total da compra é de R$ {qtd * preco * 0.95:.2f}')
elif forma_de_pgt == 3:
    print(f'Valor total da compra é de R$ {qtd * preco:.2f}')
elif forma_de_pgt == 4:
    print(f'Valor total da compra é de R$ {qtd * preco * 1.1:.2f}')
else:
    print('Código inválido!\n'
          'Tente novamente.')