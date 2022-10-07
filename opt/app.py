import os
from flask import Flask
from flaskext.mysql import MySQL      # For newer versions of flask-mysql
# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__)

mysql = MySQL()

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'db_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Passw0rd'
app.config['MYSQL_DATABASE_DB'] = 'employee_db'
app.config['MYSQL_DATABASE_HOST'] = mysql_database_host
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

# ergänzt von Ulrike
TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
#    "  `birth_date` date NOT NULL,"
    "  `name` varchar(14) NOT NULL,"
    "  `age` int(2) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
#    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
# cursor.execute(" CREATE TABLE employees('id' int(11) NOT NULL AUTO_INCREMENT,'name' varchar(14) NOT NULL, 'age' int(2), 'gender' enum ('M','F') NOT NULL, PRIMARY KEY ('name')) ENGINE=InnoDB")
cursor.execute(" DROP TABLE IF EXISTS employees")
cursor.execute(TABLES['employees'])
cursor.execute(" INSERT INTO employees (name, age, gender) VALUES('John',21,'M') ")
cursor.execute(" INSERT INTO employees (name, age, gender) VALUES('Clare',21,'F') ")
cursor.execute(" INSERT INTO employees (name, age, gender) VALUES('Jacob',18,'M') ")
#Saving the Actions performed on the DB
conn.commit()

# ende Ulrike

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/read from database')
def read():
    cursor.execute("SELECT * FROM employees")
# lösung 1:
# Ausgabe: 1,John,21,M,2,Clare,21,F,3,Jacob,18,M
#    row = cursor.fetchone()
#    result = []
#    while row is not None:
#      result.append(str(row[0]))
#      result.append(row[1])
#      result.append(str(row[2]))
#      result.append(row[3])
#      row = cursor.fetchone()

#    return ",".join(result)

# Lösung 2: ist eleganter
# Ausgabe: (1,John, 21,M),(2,Clare,21,F),(3,Jacob,18,M)

    records = cursor.fetchall()
    result = []

    for row in records:
        result.append(row)

    return ",".join(str(x) for x in result)

if __name__ == "__main__":
    app.run()
