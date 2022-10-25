import requests
from bs4 import BeautifulSoup
import pandas as pd
data = []
url = "https://lista.mercadolivre.com.br/"
produto = input("Qual produto deseja pesquisar? ")

response = requests.get(url + produto)

pesquisa = BeautifulSoup(response.text, "html.parser")

produtos = pesquisa.findAll("div", attrs={"class": "andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core ui-search-result--advertisement andes-card--padding-default"}) 

for produto in produtos:
  titulo = produto.find("h2", attrs={"class":"ui-search-item__title shops__item-title"})
  link = produto.find("a", attrs={"class":"ui-search-item__group__element shops__items-group-details ui-search-link"})
  
  simbol = produto.find("span", attrs={"class":"price-tag-symbol"})
  real = produto.find("span", attrs={"class":"price-tag-fraction"})
  virgula = produto.find("span", attrs={"class":"price-tag-decimal-separator"})
  centavos = produto.find("span", attrs={"class":"price-tag-cents"})
  
  print(titulo.text)
  print(link["href"])
  
  if centavos:
    valor = simbol.text + real.text + virgula.text + centavos.text
    data.append([titulo.text, link["href"], valor])
    print("\n\n")
    
  else:
    valor = simbol.text + real.text
    data.append([titulo.text, link["href"], valor])
    print("\n\n")

df = pd.DataFrame(data, columns=["Título", "Link", "Preço"])
print(df)
df.to_excel("Naruto.xlsx", index=False)
