print("==="*20)
produto = float(input('qual o valor do produto: '))
print('ESCOLHA UMAS DAS OPÇÕES\n [1] DINHEIRO/CHEQUE\n [2] À VISTA CARTÃO\n [3] 2X NO CARTÃO\n [4] 3X OU MAIS NO CARTÃO')
pagamento = int(input('QUAL O METODO DE PAGAMENTO: '))
#a vista 10% de desconto 
#a vista no cartão 5% de desconto
#duas vezes o preço fica no normal
#3x ou mais no cartão recebe 20% de juros
if pagamento == 1:
    desconto = (produto * 10) / 100
    total = produto - desconto
    print('seu produto que custou R$:{} com 10% de desconto fica por R$:{}'.format(produto, total))
elif pagamento == 2:
    desconto = (produto * 5) / 100
    total = produto - desconto
    print('seu produto que custou R$:{} com 5% de desconto fica por R$:{}'.format(produto, desconto))
elif pagamento == 3:
    parcela = produto / 2
    print('seu produto de R$:{} parcelando em 2x de {}'.format(produto, parcela))
elif pagamento == 4:
    parcelas = int(input('em quantas parcelas deseja pagar: '))
    total = (produto * 20) / 100
    tos = total + produto
    subtotsl = tos / parcelas
    print('seu produto de R$:{}, parcelando em {} sai por R$:{}'.format(produto, parcelas, subtotsl))