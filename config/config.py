from library import get_config

# carrega parametros
config = get_config() 

# folders
dir = config["files"]["dir"]
columns_default = config["columns_default"]


# database:
host = config["engine"]["host"]
database = config["engine"]["database"]
user = config["engine"]["user"]
pwd = config["engine"]["password"]
table = config["engine"]["table_name"]




  



