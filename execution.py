import pyodbc as db
from connections import getConnection
import io

def getSQL(fileName: str):
    sql = ''
    with open(f'SQLs\{fileName}.sql', 'r', encoding='UTF-8')as f:
        sql += f.read()
    return sql
    

def execSQL():
    connectionString, sqlFileName = getConnection()
    sql = getSQL(sqlFileName)

    try:
        connection = db.connect(connectionString)
        exec = connection.cursor()
        response = exec.execute(sql)
        # print(response.rowcount)
        response.commit()

        # lines = exec.fetchall()

        # for line in lines: 
        #     print(str(line))
    except (db.Error) as e:
        print(f"Erro ao executar script na base de dados: \n {e}")
        return "Error"
    
