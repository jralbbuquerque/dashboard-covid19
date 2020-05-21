#!/usr/bin/python
# -*- coding: utf-8 -*-

# Este script é responsável por ler o arquivo de dados de covid-19
# na pasta datsrc e transformalo em datasets mais organizados e 
# legíveis pelo PowerBI, diminuindo a quantidade de pré processamento
# realizado na ferramenta.

## Import libraries
import pandas as pd
import time
import datetime as dt

## Inicializa o timer de execução
print("Iniciado em: {}\n".format(dt.datetime.now()))
start_time = time.time()

# Log para usuário
print('Processando...\n')

### Lê a fonte de dados
df = pd.read_excel('./datasrc/HIST_PAINEL_COVIDBR_20mai2020.xlsx')

### Cria o dataset de municípios
df_city = df[df['municipio'].notnull()]
df_city = df_city.fillna(0)

### Cria o dataset de estados
df_state = df[(df['municipio'].isnull()) & (df['estado'].notnull())]
df_state = df_state.drop(['municipio', 
                          'codmun', 
                          'codRegiaoSaude', 
                          'nomeRegiaoSaude', 
                          'emAcompanhamentoNovos'], axis=1)
df_state = df_state.fillna(0)

### Cria o dataset de país
df_country = df[(df['municipio'].isnull()) & (df['estado'].isnull())]
df_country = df_country.drop(['municipio', 
                              'codmun', 
                              'estado',
                              'codRegiaoSaude', 
                              'nomeRegiaoSaude', 
                              'emAcompanhamentoNovos'], axis=1)

df_country = df_country.fillna(0)
df_country['casosPorDia'] = df_country['casosAcumulado'].diff().fillna(0)
df_country['obitosPorDia'] = df_country['obitosAcumulado'].diff().fillna(0)

### Transforma os dataframes em arquivos .xlsx para serem lidos no PowerBI
df_city.to_excel('./datasets/dataset_covid_city.xlsx')
df_state.to_excel('./datasets/dataset_covid_state.xlsx')
df_country.to_excel('./datasets/dataset_covid_country.xlsx')

# Print out elapsed time
elapsed_time = (time.time() - start_time) / 60
print("Finalizado em: {}. ".format(dt.datetime.now()), end="")
print("Tempo de execução: {0:0.4f} minutes.".format(elapsed_time))