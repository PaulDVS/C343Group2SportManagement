import MySQLdb


def myConnection(): #Paul's connection info
    connection_Config_Dict = {
        'user' : 'root',
        'password' : 'root',
        'host' : '127.0.0.1',
        'database' : 'sportmanagementsystem',
        'port': 3351,
        'raise_on_warnings': True,
        'auto-commit':True,
    }
    return connection_Config_Dict


def aadil_connection():

    connection_config_dict = {
        'user' : 'root',
        'password': 'Aadil123!',
        'host' : 'localhost',
        'database' : 'sportmanagementsystem'
    }

    return connection_config_dict

def doha_myConnection():
    connection_config_dict = {
        'user' : 'root',
        'password' : 'SaDa2903!',
        'host' : 'localhost',
        'database' : 'sportmanagementsystem',
    }
    return connection_config_dict




