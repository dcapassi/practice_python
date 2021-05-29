from db.checkIfDatabaseExists import checkIfDatabaseExists


def createDatabase(sqlConnection, databaseName):
    exitCode = 0
    if sqlConnection.is_connected():
        if checkIfDatabaseExists(sqlConnection, databaseName) == 0:
            try:
                mycursor = sqlConnection.cursor()
                mycursor.execute("CREATE DATABASE "+databaseName)
                exitCode = 1
                print("The database: '"+databaseName +
                      "' was successfully created")

            except:
                exitCode = -1
            finally:
                return exitCode
