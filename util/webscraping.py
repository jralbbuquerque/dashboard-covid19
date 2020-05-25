# Importa as libraries 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import warnings

# Ignora os warnings
warnings.filterwarnings('ignore') 

def scraping_data_covid(url):
  # Define o objeto option
  option = Options()

  # Salva o arquivo no diretório especificado
  option.add_experimental_option("prefs", 
                  {"download.default_directory": "C:\\Users\\Junior\\Documents\\Dev\\dashboard-covid19\\datasrc\\"})

  # Atribui a variável driver o objeto webdriver com as pré-definições
  driver = webdriver.Chrome(r"C:\Users\Junior\AppData\Local\Programs\Python\Python36\chromedriver.exe", chrome_options=option)

  # Maximiza a página
  driver.maximize_window()

  # Inicializa o chrome com a URL 
  driver.get(url)

  # Espera 5 segundo para o carregamento de toda a página
  time.sleep(5)

  # Localiza o botão de download 
  driver.find_element_by_xpath(
      "//*[@class='btn-white md button button-solid button-has-icon-only ion-activatable ion-focusable hydrated']").click()

  # Espera 10 segundos para o arquivo ser baixado
  time.sleep(10)

  # Fecha a página
  driver.quit()