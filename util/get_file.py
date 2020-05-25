from pathlib import Path

def most_recent_file(path):
  """Encontra o arquivo mais recente em um determinado
    diretório.

  Parâmetros
  ----------
  path : str
      Diretório a ser analisádo

  Retorno
  -------
      recent_file : str
        Arquivo mais recente
  """

  # Identifica as datas de modificação
  data_modificacao = lambda f: f.stat().st_mtime

  # Encontra o diretório no qual estão os arquivos
  directory = Path(path)

  # Seleciona apenas os arquivos com extensão .xlsx
  files = directory.glob('*.xlsx')

  # Ordena os arquivos do mais recente para o menos recente
  recent_file = str(sorted(files, key=data_modificacao, reverse=True)[0])

  return recent_file