# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
# https://www.youtube.com/watch?v=hQl2wyJvK5k
from mysql.connector import (connection)

cnx = connection.MySQLConnection(
    user='jose', password='1234',
    host='127.0.0.1',
    database='flaskrest'
)

my_cursor = cnx.cursor()
my_cursor.execute("SHOW DATABASES")

for d in my_cursor:
    print(d)

cnx.close()
print(1)