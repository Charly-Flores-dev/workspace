import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ilusion1!!*',
    database='prueba',
)

cursor = midb.cursor()
#listar datos
#cursor.execute('select * from Usuario')
#resultado = cursor.fetchall()
#print(resultado)

cursor.execute('select * from Usuario limit 1')
resultado = cursor.fetchall()
print(resultado)

#ver definicion de datos
#cursor.execute('show create table Usuario')

#insertar datos

#sql = 'insert into Usuario(email, username, edad) values(%s, %s, %s)'
#values = ('mirnasierra92@gmail.com', 'mi amor', 30)

#actualizar datos
#sql = 'update Usuario set email= %s where id=%s'
#values= ('mirnasierra92@outlook.com',4)
#cursor.execute(sql,values)

#midb.commit()

#print(cursor.rowcount)

#eliminar datos
#sql ='delete from Usuario where id=%s'
#values=(4, )
#cursor.execute(sql,values)
#midb.commit()


