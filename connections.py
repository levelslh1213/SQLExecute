import configparser as cp
import cryptocode as cc

def getConnection ():
    passwordKey = "Execution"
    config = cp.ConfigParser()
    config.read('params.ini')

    try:
        serverAddress = config.get('ConnectionString', 'ServerAddress')
        database = config.get('ConnectionString', 'Database')
        userName = config.get('ConnectionString', 'UserName')
        password = cc.decrypt(config.get('ConnectionString', 'Password'), passwordKey)
        connectionString = (
            f"DRIVER=ODBC Driver 17 for SQL Server;"
            f"SERVER={serverAddress};"
            f"DATABASE={database};"
            f"UID={userName};"
            f"PWD={password}"
        )
    except cp.Error as e:
        return None, None
    
    return connectionString