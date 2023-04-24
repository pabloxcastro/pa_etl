import boto3
from library import get_config


# carrega parametros
config = get_config() 

access_key = config["aws"]["access_key"]
secret_key = config["aws"]["secret_key"]

s3 = boto3.client(
    service_name = 's3',
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key,
    region_name = 'us-east-2'
)

# folders
obj_bronze = config["files"]["obj_bronze"]
obj_prata = config["files"]["obj_prata"]
obj_ouro = config["files"]["obj_ouro"]
obj_log = config["files"]["obj_log"]

file_ieee_brz = config["files"]["ieee_brz"]
file_ieee_prt = config["files"]["ieee_prt"]
file_sd_brz = config["files"]["sd_brz"]
file_sd_prt = config["files"]["sd_prt"]
file_all_ouro = config["files"]["all_ouro"]
file_log = config["files"]["log"]

bucket = config["files"]["bucket"]  
dir = config["files"]["dir"]

columns_default = config["columns_default"]

# database:
host = config["engine"]["host"][1]
database = config["engine"]["database"][1]
user = config["engine"]["user"]
pwd = config["engine"]["password"][1]
table = config["engine"]["table_name"]




  



