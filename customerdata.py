from faker import Faker
import time
import utils
from dbConnectionDetails import dbConnection

class Customer:
    def __init__(self) -> None:
        self.CustomerName = ''
        self.CustomerAddress = ''
        self.CustomerSSN = ''
        self.CustomerCity = ''
    
    def genFakeData(self, fake):
        self.CustomerName = fake.name()
        self.CustomerAddress = fake.address().strip().replace('\n', ' ')
        self.CustomerSSN = fake.ssn()
        self.CustomerCity = fake.city()

def main():
    fake = Faker()
    sleepTime = 1 * 60
    # sleepTime = 5
    tableName = 'customer'
    schemaName = 'dev'

    while(1):
        customer = Customer()
        customer.genFakeData(fake)
        insertStatement = utils.prepInsertStatement(tableName = tableName, schemaName= schemaName, objectDict = customer.__dict__)
        # print(insertStatement)
        conn = utils.connectDatabase(dbConnection().__dict__)
        cur = conn.cursor()
        cur.execute(insertStatement)
        # cur.close()
        cur.close()
        conn.commit()
        conn.close()
        time.sleep(sleepTime)

if __name__ == '__main__':
    main()





