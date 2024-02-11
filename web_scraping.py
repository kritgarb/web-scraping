import requests
from bs4 import BeautifulSoup

# URL do site alvo para testes
url = 'http://quotes.toscrape.com'

# Enviar uma requisição GET para o site
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # Parse do conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Localizar os elementos HTML que contêm as informações desejadas
    quotes = soup.find_all('span', class_='text')

    # Extrair e imprimir as citações
    for quote in quotes:
        print('Citação:', quote.text)
else:
    print('Falha na requisição. Código de status:', response.status_code)
