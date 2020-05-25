## Import libraries
import pandas as pd

def preprocessamento():
  ### Lê a fonte de dados
  df = pd.read_excel('./datasrc/HIST_PAINEL_COVIDBR_24mai2020.xlsx')

  ###########################################################################################
  ### Lê o arquivo com as geolocalizações dos municípios
  df_localizacoes = pd.read_csv('./datasets/datasets_localizacao_municipios.csv')
  df_localizacoes['codmun'] = df_localizacoes['codigo_ibge']//10
  df_localizacoes = df_localizacoes[['codmun', 'latitude', 'longitude']]

  ### Cria o dataset de municípios
  df_city = df[df['municipio'].notnull()]
  df_city = df_city.fillna(0)
  df_city = pd.merge(df_city, df_localizacoes, on='codmun')

  ### Adiciona nome completo dos estados brasileiros
  estados = {'Acre': 'AC',
            'Alagoas': 'AL',
            'Amapá': 'AP',
            'Amazonas': 'AM',
            'Bahia': 'BA',
            'Ceará': 'CE',
            'Distrito Federal': 'DF',
            'Espírito Santo': 'ES',
            'Goiás': 'GO',
            'Maranhão': 'MA',
            'Mato Grosso': 'MT',
            'Mato Grosso do Sul': 'MS',
            'Minas Gerais': 'MG',
            'Pará': 'PA',
            'Paraíba': 'PB',
            'Paraná': 'PR',
            'Pernambuco': 'PE',
            'Piauí': 'PI',
            'Rio de Janeiro': 'RJ',
            'Rio Grande do Norte': 'RN',
            'Rio Grande do Sul': 'RS',
            'Rondônia': 'RO',
            'Roraima': 'RR',
            'Santa Catarina': 'SC',
            'São Paulo': 'SP',
            'Sergipe': 'SE',
            'Tocantins': 'TO'} 

  df_estados_siglas = pd.DataFrame(list(estados.items()), columns='uf estado'.split())
  df_city = pd.merge(df_city, df_estados_siglas, on='estado')

  ###########################################################################################
  ### Cria o dataset de estados
  df_state = df[(df['municipio'].isnull()) & (df['estado'].notnull())]
  df_state = df_state.drop(['municipio', 
                            'codmun', 
                            'codRegiaoSaude', 
                            'nomeRegiaoSaude', 
                            'emAcompanhamentoNovos'], axis=1)
  df_state = df_state.fillna(0)

  ###########################################################################################
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

  ###########################################################################################
  ### Transforma os dataframes em arquivos .xlsx para serem lidos no PowerBI
  df_city.to_excel('./datasets/dataset_covid_city.xlsx')
  df_state.to_excel('./datasets/dataset_covid_state.xlsx')
  df_country.to_excel('./datasets/dataset_covid_country.xlsx')