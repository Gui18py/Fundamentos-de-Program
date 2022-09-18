import pandas as pd
import time

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