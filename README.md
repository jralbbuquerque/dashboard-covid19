# Dashboard COVID-19

<p align="center">
  <a href="#-overview">Overview</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-utilizar">Como utilizar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>

<h1 align="center">
    <img alt="Dashboard" title="#delicinha" src="images/imagem_dashboard.png" width="500px" />
</h1>

## 💻 Overview
Este repositório contêm um projeto de dashboard para monitoramento de dados do COVID-19, para o Brasil e seus estados e municípios, desenvolvido com Power BI e Python 3. O painel está disponível [neste link](https://app.powerbi.com/view?r=eyJrIjoiNjUwY2M5YzctMmZhYy00NzBlLTg5ZjgtNmMwZjIzYWIwNmMyIiwidCI6IjVjODg0N2M3LTZiNjQtNDNmMC04ZTg4LWMyNTA5OTgyNTQ5ZiJ9) e é atualizado diariamente com dados do [Ministério da Saúde](https://covid.saude.gov.br/).

## :rocket: Tecnologias
Esse projeto foi desenvolvido com as seguintes técnologias:
* [Python 3](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Selenium](https://www.selenium.dev/)
* [Power BI](https://powerbi.microsoft.com/pt-br/)

## 🤔 Como utilizar
Faça o clone deste repositório:
`$ git clone https://github.com/jralbbuquerque/dashboard-covid19.git`

Instale as dependências necessárias:
`$ pip install -r requirements.txt`

Execute o arquivo `main.py` responsável por realizar o scraping e pré-processamento dos dados, posteriormente salvando-os na pasta `.\datasets\`: 
`$ python main.py`

Obs: para a utilização do Selenium em navegadores padrões, como o Google Chrome, é necessário instalar o driver do navegador. [Neste link](https://medium.com/nexoos/usando-selenium-chrome-driver-e-capybara-para-automatizar-relat%C3%B3rios-web-459f949c75e5) é explicando de forma simplificada como ocorre essa configuração.

Uma vez que os dados foram baixados e tratados, abra o arquivo `Painel COVID-19.pbix` utilizando o Power BI e atualize o painel com os novos dados.

## :memo: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.
