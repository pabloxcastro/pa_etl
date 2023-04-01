import os
import requests
import pandas as pd
from config.config import *
from library import clean_year

def getUrlApi_sd(startPage, count):
    url_api = config["api_sd"]["uri"]
    url_api += "apikey=" + config["api_sd"]["apiKey"]
 
    if config["api_sd"]["query"]:
        url_api += "&query=" + config["api_sd"]["query"]

    url_api += "&startPage=" + str(startPage)
    url_api += "&count=" + str(count)   

    return url_api    


def extract_sd() -> pd.DataFrame:

    count = 50
    startPage = 1
    total_records = 1
    
    df_sd_bronze = pd.DataFrame()

    while total_records > 0:

        url_api = getUrlApi_sd(startPage, count)

        response = requests.get(url_api)

        if response.status_code == 200:

            dados_sd = response.json()

            articles  = dados_sd["search-results"]["entry"]
            df_articles = pd.DataFrame(articles)
            
            df_articles["load-date"] = clean_year(df_articles["load-date"])
            df_articles = df_articles.replace("'", "", regex=True)
            
            df_sd_bronze = pd.concat([df_sd_bronze, df_articles])

            if total_records == 1:
                total_records = int(dados_sd["search-results"]["opensearch:totalResults"])

        os.system('clear')
        startPage += count
        total_records -= count

        if total_records < 0:
            total_records = 0

        print("Science Direct: " + url_api)
        print("Total de registros faltantes: ", total_records)
        print("Total de registros minerados: ", df_sd_bronze.shape[0])
        print("Total de registros encontrados: ", str(total_records + df_sd_bronze.shape[0]))       
   
    return  df_sd_bronze
 
        
                










    


