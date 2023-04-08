from sqlalchemy import create_engine
from config.config import *
from library import select_col
from extraction_ieee import *
from extraction_sd import *


if __name__ == "__main__":
    
    # Camada Bronze
    # extraindo sd 
    df_sd_bronze = extract_sd()
    df_sd_bronze.to_excel(f'{dir}/df_sd_bronze.xlsx', index = False)

    # extraindo ieee
    df_ieee_bronze = extract_ieee()
    df_ieee_bronze.to_excel(f'{dir}/df_ieee_bronze.xlsx', index = False)  

    # Camada prata
    # padronizando colunas sd
    df_sd_prata = select_col(df_sd_bronze, columns_default)                     
    df_sd_prata.to_excel(f'{dir}/df_sd_prata.xlsx', index = False) 

    # padronizando colunas ieee
    df_ieee_prata = select_col(df_ieee_bronze, columns_default)                     
    df_ieee_prata.to_excel(f'{dir}/df_iee_prata.xlsx', index = False) 

    # Camada Ouro 
    # consolidando planilhas
    df_all_ouro = pd.concat([df_sd_prata, df_ieee_prata])
    df_all_ouro.to_excel(f'{dir}/df_all_ouro.xlsx', index = False)

    # Inserindo no banco de dados
    engine = create_engine(f'postgresql://{user}:{pwd}@{host}:5432/{database}')
    df_all_ouro.to_sql(table, engine, if_exists='replace', index=True)

 
        
                










    


