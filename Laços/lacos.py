import pandas as pd
import statistics as sts
import numpy as np
import time

"""O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50"""
"""
tabela_precos = []
for produto in range(1, 51):
    valor = 1.99 * produto
    tabela_precos.append([produto, valor])
precos = pd.DataFrame(tabela_precos, columns=["Quantidade", "Preço de Venda"])
print(precos)"""

"""O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...

print("Lojas Tabajara")
qtd_produtos = int(input("Quantos produtos foram comprados? "))
total = 0
for produto in range(1, qtd_produtos + 2):
    valor = float(input(f"Qual o valor do produto {produto}? "))
    total += valor
    time.sleep(0.5)

    if valor == 0:
        print(f"Total: R$ {total}")
        dinheiro = float(input("Qual o valor que será dado para pagamento? "))
        print(f"Dinheiro: R$ {dinheiro}")
        if total == dinheiro:
            print("O valor pago foi exato")
        elif total < dinheiro:
            troco = dinheiro - total
            print(f"Troco: R$ {troco}")
print("Muito obrigado, volte sempre!!!")"""

"""O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00"""

"""tabela_pao = []
preco_pao = 0.18
for qtd_pao in range(1, 51):
    valor = qtd_pao * preco_pao
    tabela_pao.append([qtd_pao, valor])

paes = pd.DataFrame(tabela_pao, columns=["Qtd de Pães", "Valor"])
print(paes)"""

"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas."""

"""lista = [15.7, 25.6, 12, 20, 40.6, 50.7]

maximo = max(lista)
minimo = min(lista)
media = sts.mean(lista)

print(f"Os valores da base de dados são: Máximo: {maximo}C°, Mínimo: {minimo}C°, Média: {media:.2f}")"""

"""Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""
"""divida = []
valor_inicial = 1000
porcent_parcela = 10
for i in range(3, 10, 3):
    qtd_parcela = i
    valor_juros = (porcent_parcela/100 * valor_inicial)
    valor_divida = valor_inicial + valor_juros
    valor_parcela = valor_divida / qtd_parcela
    divida.append([valor_divida, valor_juros, qtd_parcela, valor_parcela])
    porcent_parcela += 5

tabela_divida = pd.DataFrame(divida, columns = ["Valor da Divida", "Valor dos Juros", "Quantidade de Parcelas", "Valor da Parcela"])
print(tabela_divida)"""

"""O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e 
as quantidades desejadas. Calcule e mostre o valor a ser 
pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado."""

produto = {
    "Cachorro Quente": {
    "codigo": 100,
    "preco": 1.20

}, "Bauru Simples":{
    "codigo": 101,
    "preco": 1.30

}, "Bauru com Ovo": {
    "codigo": 102,
    "preco": 1.50

}, "Hambúrguer": {
    "codigo": 103,
    "preco": 1.20

}, "Cheeseburguer": {
    "codigo": 104,
    "preco": 1.30

}, "Refrigerante": {
    "codigo": 105,
    "preco": 1
}}

prod = []
for produtos, preco_cod in produto.items():
    codigo = []
    preco = []
    for codigo_preco, precos_valores in preco_cod.items():
        if codigo_preco == "codigo":
            codigo.append(precos_valores)
        if codigo_preco == "preco":
            preco.append(f"R$ {precos_valores:.2f}")
    prod.append([produtos, *codigo, *preco])    
cardapio = pd.DataFrame(prod, columns=["Especificação", "Código", "Preço"])

print("Seja bem vindo!!! \n Irei te apresentar o nosso cardápio:")
print()
time.sleep(0.5)
print("Por favor, escolha um item :)")
print()
time.sleep(0.5)
print(cardapio)
time.sleep(0.5)
while True:

    usu = int(input("Digite um código: "))
    print()
    for produtos, preco_produto in produto.items():
        for pre_prod, valores, in preco_produto.items():
            if usu == valores:
                print(f"O pedido é: {produtos} - {valores}")
                print()
                qtd = int(input("Qual será a quantidade de porções: "))
                print()
                for i, c in preco_produto.items():
                    if i == "preco":
                        novo_valor = c * qtd 
                        print(f"O preço de {qtd} porções de {produtos} será: R${novo_valor:.2f}")
                        print()
                        
    pedido = input("Deseja fazer outro algum pedido? [s/n] ")
    print()
    pedido = pedido[0].lower()

    if pedido == "n":
        break
print("Os pedidos sairão em breve!!!")
time.sleep(0.5)
print("Muito obrigado pela preferência, volte sempre!!!")