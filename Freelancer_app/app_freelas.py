# acessar o site
#https://www.terabyteshop.com.br/pc-gamer/t-gamer
# extrair todos os títulos
# extrair todos os preços
# inserir os títulos e preços na planilha
# Como entregar para o cliente

#Importando as bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

#Acessando o site
driver_site = webdriver.Chrome()
driver_site.get('https://www.terabyteshop.com.br/pc-gamer/t-gamer')
#Extrair todos os títulos
titulo = driver_site.find_elements(By.XPATH, "//a[@class='prod-name']")
#Extrair todos os preços

preco = driver_site.find_elements(By.XPATH, "//div[@class='prod-new-price']")

#Criando a planilha
workbook = openpyxl.Workbook()
#Criando a página "Produtos"
workbook.create_sheet('PRODUTOS')
#Seleciono a página produtos
sheet_produtos = workbook['PRODUTOS']
sheet_produtos['A1'].value = "PRODUTO"
sheet_produtos['B1'].value = "PREÇOS"
workbook.save("produtos.xlsx")


#inserir os títulos e os preços na planilha
for titulo, preco in zip (titulo, preco):
    sheet_produtos.append([titulo.text, preco.text])

workbook.save('produtos.xlsx')