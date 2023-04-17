
from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import datetime

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# List of all roads with status 
@app.route('/query')
def query():
    conn = sqlite3.connect("road.db")
    cur = conn.execute("SELECT * FROM road")
    rows=cur.fetchall()
    conn.commit()
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%y-%m-%d")

    return render_template('index.html',time=time,date=date,rows=rows)
 
# retreiving data from server which is sent by water level sensor(FloatSensor) Location 580037
@app.route('/560037/<int:d>')
def Outer_Ring_Road(d):
    conn = sqlite3.connect("road.db")
    conn.execute("UPDATE road SET Status=? WHERE pincode=560037",(d,))
    conn.commit()
    return redirect('/query')

# retreiving data from server which is sent by water level sensor(FloatSensor) at Location 580068

@app.route('/560068/<int:d>')
def Silk_Board_junction_road(d):
    conn = sqlite3.connect("road.db")
    conn.execute("UPDATE road SET Status=? WHERE pincode=560068",(d,))
    conn.commit()
    return redirect('/query')


if __name__ == "__main__":
    app.run(debug=True, port=500)
