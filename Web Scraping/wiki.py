import requests
from bs4 import BeautifulSoup

url = "https://pt.wikipedia.org/wiki/"
usuario = input("O que deseja pesquisar? ")

response = requests.get(url + usuario)

site = BeautifulSoup(response.text, "html.parser")

pesquisa = site.find("div", attrs={"class":"mw-content-container"})

titulo = pesquisa.find("span", attrs={"class":"mw-page-title-main"})
print(titulo.text)
