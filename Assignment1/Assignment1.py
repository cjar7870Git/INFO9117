from flask import Flask, request, render_template
import sqlite3



app = Flask(__name__)
host="localhost"
port="5000"
address="http://{0}:{1}".format(host,port)
conn = sqlite3.connect('BlueFarm.db')
c = conn.cursor()

users = {"test":"test123", "admin":"admin","newUser1":"newPassword1"}

def serve_forever():
    app.run(host, port)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with Werkzeug server")
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db_passwd = users.get(username)
        if password == db_passwd:
            return "Success"
        else:
            return "Fail"
    else:
        return render_template("login.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in c.execute('SELECT username FROM Users'):        #if username not in users:
           c.execute("INSERT INTO Users VALUES(username, password)")
           conn.commit()
           users[username] = password
           #print(users)
           return "Success"
        else:
           return "Fail"

    else:
        return render_template("register.html")



if __name__ == '__main__':
    serve_forever()