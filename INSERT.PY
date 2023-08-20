import mysql.connector

conector = mysql.connector.connect(use='root', password='', host='127.0.0.1', database = 'testepython')

query = ("INSERT INTO TB001_Cores (C001_Nome) VALUES ('Verde')")
cursor = conector.cursor()
cursor.execute(query)
conector.commit
conector.close()
