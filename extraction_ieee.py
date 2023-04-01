import os
import requests
import pandas as pd
from config.config import *
from library import explode_authors, explode_keywords

def getUrlApi_ieee(start, max):
    url_api = config["api_ieee"]["uri"]
    url_api += "format=json"
    url_api += "&apikey=" + config["api_ieee"]["apikey"]     

    if config["api_ieee"]["abstract"]:
        url_api += "&abstract=" + config["api_ieee"]["abstract"]

    if config["api_ieee"]["article_title"]:
        url_api += "&article_title=" + config["api_ieee"]["article_title"]

    if config["api_ieee"]["author"]:
        url_api += "&author=" + config["api_ieee"]["author"]

    url_api += "&start_record=" + str(start)
    url_api += "&max_records=" + str(max)

    return url_api


def extract_ieee() -> pd.DataFrame:
    
    max_records = 50
    start_record = 1
    total_records = 1
    
    df_ieee_bronze = pd.DataFrame()

    while total_records > 0:

        url_api = getUrlApi_ieee(start_record, max_records)

        response = requests.get(url_api)

        if response.status_code == 200:

            dados_ieee = response.json()

            articles  = dados_ieee["articles"]
            df_articles = pd.DataFrame(articles)

            df_articles["authors"] = explode_authors(df_articles["authors"])  
            df_articles["index_terms"] = explode_keywords(df_articles["index_terms"])                        
            df_articles = df_articles.replace("'", "", regex=True)        

            df_ieee_bronze = pd.concat([df_ieee_bronze, df_articles])

            if total_records == 1:
                total_records = dados_ieee["total_records"]

        os.system('clear')
        start_record += max_records
        total_records -= max_records

        if total_records < 0:
            total_records = 0

        print("IEEE: " + url_api)
        print("Total de registros faltantes: ", total_records)
        print("Total de registros minerados: ", df_ieee_bronze.shape[0])
        print("Total de registros encontrados: ", str(total_records + df_ieee_bronze.shape[0]))       

    return df_ieee_bronze


