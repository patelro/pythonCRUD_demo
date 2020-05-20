# [START gae_python37_cloudsql_mysql]
import os

from flask import Flask, render_template, request, redirect
import pymysql

# environment varibales
db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

unix_socket = '/cloudsql/{}'.format(db_connection_name)
cnx = pymysql.connect(user=db_user, password=db_password,
                      unix_socket=unix_socket, db=db_name)


app = Flask(__name__)


# adding users to the database
@app.route('/', methods=['GET', 'POST'])
def index():

    cursor = cnx.cursor()

    if request.method == 'POST':
        # getting user entery
        fname = request.form['firstName']
        lname = request.form['lastName']
        userName = request.form['userName']

        # query to insert a new user
        query = "insert into users_tbl(first_name,last_name,user_name) values (%s, %s, %s);"
        val = (fname, lname, userName)

        # making sure data is inserted
        try:
            cursor.execute(query, val)
            cnx.commit()
            return redirect('/')
        except:
            return 'There was a problem inserting to the database'

    else:
        allUsers = "select * from users_tbl;"
        cursor.execute(allUsers)
        records = cursor.fetchall()
        return render_template('index.html', records=records)


# deleting users
@app.route('/delete/<int:id>')
def delete(id):

    query = "delete from users_tbl where user_id = %s;"
    userID = id

    cursor = cnx.cursor()
    try:
        cursor.execute(query, userID)
        cnx.commit()
        return redirect('/')
    except:
        return "There was a problem deleting the user"


# updating users
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    cursor = cnx.cursor()

    if request.method == 'POST':
        # getting user entery
        fname = request.form['firstName']
        lname = request.form['lastName']
        userName = request.form['userName']

        try:
            dataID = id
            update = "update users_tbl set first_name = %s, last_name = %s, user_name = %s where user_id = %s;"
            info = (fname, lname, userName, dataID)
            cursor.execute(update, info)
            cnx.commit()
            return redirect('/')
        except:
            return "There was an issue updating the user"
    else:
        query = "select * from users_tbl where user_id = %s;"
        userID = id
        cursor.execute(query, userID)
        record = cursor.fetchone()
        return render_template('update.html', record=record)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
