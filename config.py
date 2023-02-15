from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'sathvik'
app.config['MYSQL_DATABASE_PASSWORD'] = 'S@thvikkk2022'
app.config['MYSQL_DATABASE_DB'] = 'application'
app.config['MYSQL_DATABASE_HOST'] = '43.205.124.87'

#public ip of mysql server instance.

mysql.init_app(app)
