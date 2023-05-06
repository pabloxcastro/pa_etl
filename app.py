from sqlalchemy import create_engine
from config.config import *
from library import select_col
from extraction_ieee import *
from extraction_sd import *


if __name__ == "__main__":

    # LENDO FONTE DE DADOS
    # SD - Extraindo 
    
    df_sd_bronze = extract_sd()
    log_text = f"SD - Dados lidos - linhas: {df_sd_bronze.shape[0]} e colunas: {df_sd_bronze.shape[1]}"
    Log_pa.log_write(log_text)

    df_sd_bronze.to_excel(f'{dir}/{file_sd_brz}', index = False)
    Log_pa.log_write(f"SD - planilha bronze criada {dir}/{file_sd_brz}")

    s3.upload_file(f"{dir}/{file_sd_brz}", bucket, f"{obj_bronze}/{file_sd_brz}")
    Log_pa.log_write(f"SD - enviado para o bucket {bucket} {obj_bronze}/{file_sd_brz}")

    # Padronizando colunas
    df_sd_prata = select_col(df_sd_bronze, columns_default)                     
    df_sd_prata.to_excel(f'{dir}/{file_sd_prt}', index = False) 
    Log_pa.log_write(f"SD - colunas pradonizadas {dir}/{file_sd_prt}")

    s3.upload_file(f"{dir}/{file_sd_prt}", bucket, f"{obj_prata}/{file_sd_prt}")        
    Log_pa.log_write(f"SD - enviado para o bucket {bucket} {obj_prata}/{file_sd_prt}")

    # IEEE - Extraindo
    df_ieee_bronze = extract_ieee()
    log_text = f"IEEE - Dados lidos - linhas: {df_ieee_bronze.shape[0]} e colunas: {df_ieee_bronze.shape[1]}"
    Log_pa.log_write(log_text)

    df_ieee_bronze.to_excel(f'{dir}/{file_ieee_brz}', index = False)
    Log_pa.log_write(f"IEEE - planilha bronze criada {dir}/{file_sd_brz}")

    s3.upload_file(f"{dir}/{file_ieee_brz}", bucket, f"{obj_bronze}/{file_ieee_brz}")    
    Log_pa.log_write(f"IEEE - enviado para o bucket {bucket} {obj_bronze}/{file_ieee_brz}")
  
    # Padronizando colunas
    df_ieee_prata = select_col(df_ieee_bronze, columns_default)                     
    df_ieee_prata.to_excel(f'{dir}/{file_ieee_prt}', index = False)
    Log_pa.log_write(f"IEEE - colunas pardronizadas {dir}/{file_ieee_prt}")

    s3.upload_file(f"{dir}/df_sd_prata.xlsx", bucket, f"{obj_prata}/{file_ieee_prt}")
    Log_pa.log_write(f"IEEE - enviado para o bucket {bucket} {obj_prata}/{file_ieee_prt}")
    
    # CONSOLIDANDO DADOS 
    df_all_ouro = pd.concat([df_sd_prata, df_ieee_prata])
    log_text = f"Planilha consolidada - linhas: {df_all_ouro.shape[0]} e colunas: {df_all_ouro.shape[1]}"
    Log_pa.log_write(log_text)

    df_all_ouro.to_excel(f'{dir}/{file_all_ouro}', index = False)
    s3.upload_file(f"{dir}/{file_all_ouro}", bucket, f"{obj_ouro}/{file_all_ouro}")        
    Log_pa.log_write(f"Planilha consolidada armazenada no bucket {bucket} {obj_ouro}/{file_all_ouro}")

    # INSERINDO NO BANCO DE DADOS
    engine = create_engine(f'postgresql://{user}:{pwd}@{host}:5432/{database}')
    df_all_ouro.to_sql(table, engine, if_exists='replace', index=True)
    Log_pa.log_write("Dados consolidados armazenados no banco de dados")

    s3.upload_file(f"{file_log}", bucket, f"{obj_log}/{file_log}")        

 
        
                










    





