
def myConnection(): #Paul's connection info
    connection_Config_Dict_Paul = {
        'user' : 'root',
        'password' : 'root',
        'host' : '127.0.0.1',
        'database' : 'sportmanagementsystem',
        'port': 3351,
        'autocommit' : True
    }

    connection_Config_Dict_Aadil = {
        'user' : 'root',
        'password': 'Aadil123!',
        'host' : 'localhost',
        'database' : 'sportmanagementsystem',
        'autocommit' : True
    }

    connection_Config_Dict_Doha = {
        'user' : 'root',
        'password' : 'SaDa2903!',
        'host' : 'localhost',
        'database' : 'sportmanagementsystem',
        'autocommit' : True
    }

    return connection_Config_Dict_Paul




