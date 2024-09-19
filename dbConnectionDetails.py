# dbConnectionDetails = {
#         "databaseName": "",
#         "databaseUser": "",
#         "databaseHost": "",
#         "databaseUserPassword": "",
#         "databasePort": ""
#     }

class dbConnection:
    def __init__(self) -> None:
        self.databaseName = "rt-data"
        self.databaseUser = "postgres"
        self.databaseHost = "rt-postgres-db.c1um2qmgm61i.us-east-1.rds.amazonaws.com"
        self.databaseUserPassword = "Stream24!2020"
        self.databasePort = "5432"