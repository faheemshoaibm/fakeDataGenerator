from faker import Faker
import time
import utils
from dbConnectionDetails import dbConnection
from datetime import datetime
import random

class Order:
    def __init__(self) -> None:
        self.CustomerId = '',
        self.ProductId = '',
        self.OrderTime = '',
        self.OrderAmount= ''
    
    def genFakeData(self, fake:Faker, schemaName, customerTableName, customerColumnName, productTableName, productColumnName):
        self.CustomerId = str(utils.randomLookup(schemaName=schemaName, tableName=customerTableName, columnName=customerColumnName))
        self.ProductId = str(utils.randomLookup(schemaName=schemaName, tableName=productTableName, columnName=productColumnName))
        self.OrderTime = str(datetime.now())
        self.OrderAmount = str(random.randint(20,1000))

def main():
    fake = Faker()
    # sleepTime = 2 * 60
    sleepTime = 1
    tableName = 'orders'
    schemaName = 'dev'
    customerTableName = 'customer'
    customerColumnName = 'CustomerId'
    productTableName = 'product'
    productColumnName = 'ProductId'
    
    while(1):
        order = Order()
        order.genFakeData(fake,schemaName, customerTableName=customerTableName, customerColumnName=customerColumnName,
            productTableName=productTableName, productColumnName= productColumnName)
        insertStatement = utils.prepInsertStatement(tableName = tableName, schemaName= schemaName, objectDict = order.__dict__)
        print(insertStatement)
        conn = utils.connectDatabase(dbConnection().__dict__)
        cur = conn.cursor()
        cur.execute(insertStatement)
        
        cur.close()
        conn.commit()
        conn.close()
        # break
        time.sleep(sleepTime)
   
if __name__ == '__main__':
    main()





