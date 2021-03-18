from flask import Flask, redirect, request, render_template
from flask_mysqldb import MySQL
import requests, json
from flask_bootstrap import Bootstrap
import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'cigarsreview'

mysql =MySQL(app)

@app.route('/createthemaindatabase', methods=['GET','POST'] )
def createthemaindatabase():
    cur = mysql.connection.cursor()
    cur.execute('''
    create table cigarreviews(
    names varchar(255),
    brands varchar(255),
    wrapper varchar(255),
    origins varchar(255),
    fillers varchar(255),
    bodys varchar(255),
    flavors varchar(255),
    strengths varchar(255),
    descriptions longtext not null
    );''')

    mysql.connection.commit()
    cur.close()

@app.route('/', methods = ['GET', 'POST'])
def homepage():
    return render_template("homepage.html")


@app.route('/review',methods=['GET','POST'])
def render_submit_template():
    return render_template('submitreview.html')


@app.route('/added', methods=['GET','POST'])
def added():
    return "review added"

@app.route("/adding_error",  methods=['GET','POST'])
def adding_error():
    return "error adding review"

@app.route('/submitreview', methods=['POST'] )
def submitreview():

    name = request.form.get("name")
    brand = request.form.get("brand")
    wrapper = request.form.get("wrapper")
    origin = request.form.get("origin")
    filler = request.form.get("filler")

    #this part will cover the body of the cigar review
    body =request.form.get("body")
    flavor = request.form.get("flavor")
    strength = request.form.get("strength")
    flavor_description = request.form.get("description")

    #inserting the values into the database
    cur = mysql.connection.cursor()
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    cur.execute('''INSERT INTO cigarreviews(names, brands, wrapper, origins, fillers, 
    bodys, flavors, strengths, descriptions) VALUES (%s, %s,%s, %s,%s, %s,
    %s, %s,%s)''', (name, brand, wrapper, origin, filler, body, flavor,
                    strength, flavor_description))
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    try:
        mysql.connection.commit()
        cur.close()
        return "added" #will be converted to an html page
    except:
        return "bad no good" #will be converted to an html page


if __name__ == '__main__':
    app.run()
