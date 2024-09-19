import psycopg2
from dbConnectionDetails import dbConnection
import random

def prepInsertStatement(tableName, schemaName, objectDict:dict):
    columnNames = ""
    for i in objectDict.keys():
        columnNames = columnNames + i + ','
    columnNames = columnNames[:-1]

    valuesString = ""
    for j in objectDict.values():
        valuesString = valuesString + "'" + j + "'" + ','
    valuesString = valuesString[:-1]
    
    insertStatement = "insert into {schema}.{table}({columnNames}) values({valuesString});".format(
        schema = schemaName, table = tableName, 
        columnNames = columnNames, valuesString = valuesString)
    return insertStatement


def connectDatabase(dbConnectionDetails):
    conn = psycopg2.connect(
        database = dbConnectionDetails['databaseName'],
        user = dbConnectionDetails['databaseUser'], 
        host= dbConnectionDetails['databaseHost'],
        password = dbConnectionDetails['databaseUserPassword'],
        port = dbConnectionDetails['databasePort']
    )
    return conn

def randomLookup(schemaName, tableName, columnName):
    conn = connectDatabase(dbConnection().__dict__)
    cur = conn.cursor()

    selectStatement = "select min({column}), max({column}) from {schema}.{table}".format(
        column = columnName, schema = schemaName, table = tableName)
    
    cur.execute(selectStatement)

    myresult = cur.fetchall()
    x = myresult[0]
    randomId = random.randint(x[0], x[1])

    cur.close()
    conn.close()

    return randomId