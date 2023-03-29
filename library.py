import pandas as pd
import numpy as np
import yaml
import psycopg as psg

# Função para criar um novo DF com as colunas do escopo baseado no DF Geral
def select_col(df_geral, columns_out) -> pd.DataFrame:
  
  new_df = pd.DataFrame()

  for value in columns_out.values():

  # interar lista de todos os tipos de colunas
    for col in value:
      # verificar se um item do tipo existe no DF
      if col in df_geral.columns:
        # se existir criar um nova coluna no new_DF com o rótulo do primeiro item da lista do tipo da coluna
        new_df[value[0]] = df_geral[col]
        break
      else:
        # se a coluna não existir então verificar se é a última coluna da lista do tipo
        # isso significa que não existe a coluna no DF, então criar um coluna com o rótulo do primeiro item 
        # com conteúdo em branco
        if col == value[-1]:
          new_df[value[0]] = np.nan

  return new_df


# funcao para ler o arquivo externo YAML
def get_config() -> dict:

  with open('./config/config.yaml', 'r') as config:
    file_yaml = yaml.safe_load(config)

  return file_yaml

def explode_authors(column_name) -> list:

  lista_coluna = []

  for item in column_name.values:
      
      for val in item.values(): 
          authors_names = ""
          for item2 in val:
              for key2,val2 in item2.items():
                  if key2 == "full_name":
                      authors_names = authors_names + val2 + ", "
          
          authors_names = authors_names[0:-2] 
          lista_coluna.append(authors_names)

  return lista_coluna

def explode_keywords(column_name) -> list:
  lista_coluna = []
  for item in column_name.values:
      keywords_itens = ""
      for val in item.values():
          for val2 in val.values():
              for item2 in val2:
                  keywords_itens = keywords_itens + item2 + ", "
                  
      keywords_itens = keywords_itens[0:-2] 
      lista_coluna.append(keywords_itens)
  return lista_coluna

def clean_year(column):
  new_col = []
  for year in column:
    new_year = year[0:4]
    new_col.append(new_year)  
  return new_col

# database
def insert_database(host, database, user, pwd, table_name):
  try:

    connection = psg.connect(
      host = host,
      database = database,
      user = user,
      password = pwd)

    cursor = connection.cursor()
    print(table_name.shape)
    for row in table_name.values:
      sql = """INSERT INTO publications (author, title, keywords, abstract, year, type_publication, doi ) 
            VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')""".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
      
      cursor.execute(sql)
      
      connection.commit()

  except (Exception, psg.DatabaseError) as error:
    msg = [error, sql]

  finally:
    if connection:
      cursor.close()
      connection.close()
      msg = ["PostgreSQL connection is closed"]
  
  return msg



 