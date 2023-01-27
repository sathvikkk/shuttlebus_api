from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'S@thvikkk2022'
app.config['MYSQL_DATABASE_DB'] = 'shuttlebus'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
#public ip of 2nd instance.
mysql.init_app(app)
