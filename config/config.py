from library import get_config

# carrega parametros
config = get_config() 

# folders
dir = config["files"]["dir"]
columns_default = config["columns_default"]


# database:
host = config["srv_database"]["srv_host"]
database = config["srv_database"]["database"]
user = config["srv_database"]["user"]
pwd = config["srv_database"]["password"]


  



