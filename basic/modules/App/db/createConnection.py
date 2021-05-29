import mysql.connector


def createConnection(DB_DADOS):
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host=DB_DADOS['host'],
            user=DB_DADOS['user'],
            password=DB_DADOS['password']
        )
    finally:
        return mydb
