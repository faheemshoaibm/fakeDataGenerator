from faker import Faker
import time
import utils
from dbConnectionDetails import dbConnection

class Product:
    def __init__(self) -> None:
        self.ProductName = ''
    
    def genFakeData(self, fake:Faker):
        self.ProductName = fake.domain_name()

def main():
    fake = Faker()
    # sleepTime = 2 * 60
    sleepTime = 3
    tableName = 'product'
    schemaName = 'dev'

    while(1):
        product = Product()
        product.genFakeData(fake)
        insertStatement = utils.prepInsertStatement(tableName = tableName, schemaName= schemaName, objectDict = product.__dict__)
        
        conn = utils.connectDatabase(dbConnection().__dict__)
        cur = conn.cursor()
        cur.execute(insertStatement)
        
        cur.close()
        conn.commit()
        conn.close()

        time.sleep(sleepTime)

if __name__ == '__main__':
    main()





