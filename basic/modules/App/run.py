from Configs import DADOS_EMAIL, DADOS_DB
from db.createConnection import createConnection
from db.createDatabase import createDatabase
from db.createTable import createTable

from mail.message import createMessage
from mail.send import sendEmail
import sys

mySqlConnection = createConnection(DADOS_DB)
if mySqlConnection == None:
    print("Please check the Db parameters")
    sys.exit()

# Creating the database
dbName = "meli_challenge"
createDatabase(mySqlConnection, dbName)


# Creating the tables
columns = "(name VARCHAR(255), address VARCHAR(255)"
createTable(mySqlConnection, dbName, 'databases', columns)

#messageString = createMessage("Diego", "Destino", "Assunto", "Esse é o corpo")
#sendEmail(DADOS_EMAIL, messageString)
