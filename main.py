import time
import pandas as pd
import openpyxl
import urllib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

contatos_df = pd.read_excel("Enviar.xlsx")

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

# find_elements_by_id procura no site elementos com um determinado id e retorna um lista com eles
# elementos com id "side" so aparecerem depois que o login é realizado
# enquanto o login não for concluido o tamanho da lista retornada será 0
while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

mensagem = "mensagem a ser enviada"

# enumerate peda o índice da tabela e armazena na variável i
for i, saudacao in enumerate(contatos_df['Saudação']):
    pessoa = contatos_df.loc[i,"Pessoa"]
    numero = contatos_df.loc[i,"Número"]
    print(numero)
    texto = urllib.parse.quote(f"{saudacao} {pessoa}! {mensagem}")  # codificação para URL
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)