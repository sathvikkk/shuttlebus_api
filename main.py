import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

#for welcoe woorld

#@app.route('/')
#def Hello_world():
 #   return "hello world"

# For adding the passenger list to database.

@app.route('/passenger/add', methods=['POST'])
def create_passenger():
    try:
        _json = request.json
        _passengername = _json['passengername']
        _phonenumber = _json['phonenumber']
        _cityname = _json['cityname']
        if _passengername and _phonenumber and _cityname and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO passengersinfo(passengername, phonenumber, cityname) VALUES(%s, %s, %s)"
            bindData = (_passengername,  _phonenumber, _cityname)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Passenger added successfully!')
            response.status_code = 200
            return response
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#  To get the list of all passenger for database.


@app.route('/passenger/all', methods=['GET'])
def passenger():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT passengername, phonenumber, cityname FROM passengersinfo")
        passengerRows = cursor.fetchall()
        response = jsonify(passengerRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#  To get the list of a particular passenger for database.


@app.route('/passenger/<string:passengername>', methods=['GET'])
def passenger_details(passengername):

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT  passengername, phonenumber, cityname FROM passengersinfo WHERE passengername =%s", passengername)
        passengerRow = cursor.fetchone()
        response = jsonify(passengerRow)
        response.status_code = 200
        if passengerRow == None:
            response = jsonify('No passenger Record Found...')
            return response
        else:
            return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#  To update list of passenger for database.


@app.route('/passenger/<string:passengername>', methods=['PUT'])
def update_passenger(passengername):
    try:
        _json = request.json
        _passengername = _json['passengername']
        _phonenumber = _json['phonenumber']
        _cityname = _json['cityname']
        if _passengername and _phonenumber and _cityname and request.method == 'PUT':
            sqlQuery = "UPDATE passengersinfo SET phonenumber=%s, cityname=%s WHERE passengername=%s"
            bindData = ( _phonenumber, _cityname, _passengername)
            conn = mysql.connect()
            cursor = conn.cursor()
            passenger_name = cursor.execute(sqlQuery, bindData)
            conn.commit()            
            if passenger_name == 1:
                response = jsonify('passenger updated successfully!')
                response.status_code = 200
                return response
            else :
                response = jsonify('Passenger not exists in Database.!')
                response.status_code = 200
                return response
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#  To delete passenger for database.


@app.route('/passenger/<string:passengername>', methods=['DELETE'])
def delete_passenger(passengername):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        passenger_name = cursor.execute("DELETE FROM passengersinfo WHERE passengername =%s", (passengername,))
        conn.commit()
        if  passenger_name == 1:
            response = jsonify('Passenger deleted successfully!')
            response.status_code = 200
            return response
        else :
            response = jsonify('Passenger not exists in Database.!')
            response.status_code = 200
            return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# For error message

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082, debug=True)
