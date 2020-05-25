#!/usr/bin/python
# -*- coding: utf-8 -*-

# Este script é responsável por ler o arquivo de dados de covid-19
# na pasta datsrc e transformalo em datasets mais organizados e 
# legíveis pelo PowerBI, diminuindo a quantidade de pré processamento
# realizado na ferramenta.

## Import libraries
import time
import datetime as dt
from util import webscraping, etl

# Log para usuário
print('#'*80)

## Inicializa o timer de execução
print("Iniciado em: {}\n".format(dt.datetime.now()))
start_time = time.time()

print('-'*80)

print('-- Download dos dados:')
print("Realizando download dos dados...")
webscraping.scraping_data_covid("https://covid.saude.gov.br/")
print("Download finalizado!")

print('-'*80)
print('-- Pré-processando os dados:')
print('Criando os datasets utilizados pelo PowerBI...\n')
etl.preprocessamento()
print('Processo finalizado!')
print('-'*80)

# Print out elapsed time
elapsed_time = (time.time() - start_time) / 60
print("\nFinalizado em: {}. ".format(dt.datetime.now()), end="")
print("Tempo de execução: {0:0.4f} minutes.".format(elapsed_time))
print('#'*80)