import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ilusion1!!*',
    database='prueba',
)

cursor = midb.cursor()

#cursor.execute('select * from Usuario')
#sql = 'insert into Usuario()'

cursor.execute('show create table Usuario')

resultado = cursor.fetchall()
print(resultado)
