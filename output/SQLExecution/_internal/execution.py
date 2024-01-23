import pyodbc as db
from connections import getConnection
import io

class Execution: 

    def __init__(self, connectionString: None, sqlFileName: None) -> None:
        self.connectionString = connectionString
        self.sqlFileName = sqlFileName
        self.connection = db.connect(self.connectionString)

    def getSQL(self):
        sql = ''
        with open(f'SQLs\{self.sqlFileName}.sql', 'r', encoding='UTF-8')as f:
            sql += f.read()
        return sql
    
    def insertExecutionLog(self, rowCount= 0, message= ""):
        
        try:
            exec = self.connection.cursor()
            script = F"INSERT INTO PRO021LOG (DATA_EXEC, GN_MESSAGE, NR_LINHAS) VALUES (GETDATE(), \'{str(message)}\', {str(rowCount)})"
            exec.execute(script)
            exec.commit()
        except db.Error as e:
            print(f"Erro ao inserir logs de execução!\n {e}")


    def execSQL(self):
        # connectionString, sqlFileName = getConnection()
        sql = self.getSQL()

        try:
            exec = self.connection.cursor()
            response = exec.execute(sql)
            response.commit()

            # lines = exec.fetchall()

            # for line in lines: 
            #     print(str(line))
        except (db.Error) as e:
            print(f"Erro ao executar script na base de dados: \n {e}")
            return "Error"
        
        return response.rowcount
        
    def endConnection(self):
        try:
            self.connection.close()
        except db.Error as e:
            print(f"Error while closing connection: {e}")
            return "Error"
        return "Connection Closed!"
        
