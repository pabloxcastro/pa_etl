#import pandas as pd
from config.config import *
from library import select_col
from extraction_ieee import *
from extraction_sd import *

def default_columns(df_bronze, source):
    df = select_col(df_bronze, columns_default)                     
    df.to_excel(f'{dir}/df_{source}_prata.xlsx', index = False) 
    return df

if __name__ == "__main__":
    
    # extraindo sd
    df_sd_bronze = extract_sd()
    df_sd_bronze.to_excel(f'{dir}/df_sd_bronze.xlsx', index = False)

    # extraindo ieee
    df_ieee_bronze = extract_ieee()
    df_ieee_bronze.to_excel(f'{dir}/df_ieee_bronze.xlsx', index = False)  

    # padronizando
    df_sd_ouro = default_columns(df_sd_bronze, 'sd')
    df_ieee_ouro = default_columns(df_ieee_bronze, 'ieee')

    # consolidando
    df_all_ouro = pd.concat([df_sd_ouro, df_sd_ouro])
    df_all_ouro.to_excel(f'{dir}/df_all_ouro.xlsx', index = False)


 
        
                










    


