#!/usr/bin/python
# -*- coding: utf-8 -*-

# Este script é responsável por ler o arquivo de dados de covid-19
# na pasta datsrc e transformalo em datasets mais organizados e 
# legíveis pelo PowerBI, diminuindo a quantidade de pré processamento
# realizado na ferramenta.

## Import libraries
import time
import datetime as dt
import configparser
from util import webscraping, etl

CONFIG_FILE = 'config.ini'

if __name__ == '__main__':
  ###########################################################################################
  # Log para usuários
  print('#'*80)

  # Lê arquivo de configuração
  try:
      config = configparser.ConfigParser()
      config.read(CONFIG_FILE)
      print('{}\'s config file read!'.format(config['DS']['NAME']))
  except:
      print('Unable to read config file ("{}")'.format(CONFIG_FILE))
      exit(-1)

  ## Inicializa o timer de execução
  print("Iniciado em: {}\n".format(dt.datetime.now()))
  start_time = time.time()

  print('-'*80)

  print('+ Download dos dados...')
  #try:
  webscraping.scraping_data_covid(config['DS']['URL'], config['DS']['PATH_DOWNLOAD'])
  #  print("+ Download finalizado!")
  #except:
  #  print("+ Erro ao realizar o download!")
  #  exit(-1)

  print('-'*80)

  print('+ Pré-processando os dados...')
  try:
    etl.preprocessamento(config['DS']['PATH'])
    print('+ Processo finalizado!')
  except:
    print('+ Erro ao realizar o pré-processamento dos dados')
    exit(-1)
  
  print('-'*80)

  # Print out elapsed time
  elapsed_time = (time.time() - start_time) / 60
  print("\nFinalizado em: {}. ".format(dt.datetime.now()), end="")
  print("Tempo de execução: {0:0.4f} minutes.".format(elapsed_time))
  print('#'*80)