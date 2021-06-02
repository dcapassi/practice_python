from Configs import DADOS_EMAIL, DADOS_DB
from db.createConnection import createConnection
from db.createDatabase import createDatabase
from db.createTable import createTable
from db.insertData import insertData

from mail.message import createMessage
from mail.send import sendEmail

import sys
import csv
import json
import os.path

mySqlConnection = createConnection(DADOS_DB)
if mySqlConnection == None:
    print("Please check the Db parameters")
    sys.exit()

# Creating the database
dbName = "meli_challenge"
createDatabase(mySqlConnection, dbName)

# Creating the tables
columns = "(uid VARCHAR(255), db_name VARCHAR(255), owner_email VARCHAR(255), manager_email VARCHAR(255), integrity VARCHAR(255), availability VARCHAR(255), confidentiality VARCHAR(255))"
tableName = 'databases_classification'
createTable(mySqlConnection, dbName, tableName, columns)


def clearDbClassification():
    return {"dn_name": None, "confidentiality": None,
            "integrity": None, "availability": None, "uid": None, "owner_email": None, "manager_email": None}


def getManagerEmail(userList, uid):
    for usuario in userList:
        if usuario['user'] == uid:
            return usuario['manager_mail']


db_classification = clearDbClassification()


def getDataAsTuple(db_classification):
    return (db_classification["uid"], db_classification["dn_name"], db_classification["owner_email"], db_classification["manager_email"], db_classification["integrity"], db_classification["availability"], db_classification["confidentiality"])


lista_usuarios = []
with open(os.path.dirname(__file__) + "/../Data/userList.csv", encoding='utf-8') as users_refer:
    users = csv.reader(users_refer, delimiter=',')
    for linha in users:
        id = linha[0]
        user = linha[1]
        state = linha[2]
        manager_mail = linha[3]
        lista_usuarios.append(
            {"id": linha[0], "user": linha[1], "state": linha[2], "manager_mail": linha[3]})

# Ler o Json e pegar os campos corretos para gravar no banco
with open(os.path.dirname(__file__) + "/../Data/dbLIst.json") as json_file:
    data = json.load(json_file)
    for p in data["db_list"]:
        try:
            db_classification["dn_name"] = p["dn_name"]
            db_classification["confidentiality"] = p["classification"]["confidentiality"]
            db_classification["integrity"] = p["classification"]["integrity"]
            db_classification["availability"] = p["classification"]["availability"]
            db_classification["uid"] = p["owner"]["uid"]
            db_classification["manager_email"] = getManagerEmail(
                lista_usuarios, db_classification["uid"])
            db_classification["owner_email"] = p["owner"]["email"]
        except:
            pass
        finally:
            print("Gravando no Banco")
            insertData(mySqlConnection, dbName, tableName,
                       getDataAsTuple(db_classification))
            db_classification = clearDbClassification()


"""
with open('dblist.json') as json_file:
    data = json.load(json_file)
#   print(data)
    for p in data["db_list"]:
        print(p)
        if p['classification']["confidentiality"] == "high":
            for usuario in lista_usuarios:
                if p['owner']['uid'] == usuario['user']:
                    print(usuario['manager_mail'])
                    DADOS_EMAIL["receiver_email"] = usuario['manager_mail']
                    # sendEmail(DADOS_EMAIL, p['dn_name'], p['owner']['name'])
"""

# messageString = createMessage("Diego", "Destino", "Assunto", "Esse é o corpo")
# sendEmail(DADOS_EMAIL, messageString)
