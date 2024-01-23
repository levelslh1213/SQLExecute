from execution import Execution
from connections import getConnection

connectionString, sqlFileName = getConnection()
execution = Execution(connectionString=connectionString, sqlFileName=sqlFileName)
rowcount = execution.execSQL()
execution.insertExecutionLog(rowCount=rowcount, message="Sucesso!")
execution.endConnection()