from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'sathvik'
app.config['MYSQL_DATABASE_PASSWORD'] = 'S@thvikkk2022'
app.config['MYSQL_DATABASE_DB'] = 'shuttlebus'
app.config['MYSQL_DATABASE_HOST'] = '13.127.94.193'
mysql.init_app(app)