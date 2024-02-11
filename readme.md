
# Web Scraping with Python

Aplicação para extrair informações da internet de forma estruturada.


## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:kritgarb/web-scraping.git
```

Instale as dependências

```bash
  pip install requests beautifulsoup4 
```

Inicie o servidor

```bash
  python web_scraping.py

```


## Funcionalidades

- Envio de Requisição HTTP: Utiliza a biblioteca requests para enviar uma requisição HTTP para o site alvo.

 - Análise de HTML: Utiliza a biblioteca BeautifulSoup para analisar o conteúdo HTML da página e criar uma representação estruturada do DOM (Document Object Model).

 - Localização de Elementos HTML: Usa métodos fornecidos pelo BeautifulSoup para localizar elementos HTML específicos com base em tags, classes ou outros atributos.

 - Extração de Dados: Extrai dados específicos (citações, no exemplo) dos elementos HTML localizados.

 - Impressão dos Resultados: Exibe os dados extraídos no console ou em outro formato desejado.


## Autores

- [@kritgarb](https://www.github.com/kritgarb)


## Referência
 - [Python](https://www.python.org/doc/) 
 - [Requests](https://pypi.org/project/requests/) 
 - [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) 
 - [Teste de web scraping](http://quotes.toscrape.com) 
 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

