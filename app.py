from flask import Flask, render_template, url_for, request, flash, redirect
from quiz import questions, answers
from db import create_table
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'random_string_for_browser_session'

answer = answers()
question = questions()

# RENDER TEMPLATES ------------------------------------------------
@app.route('/')
def home():
    create_table()
    no_db = ("DATABASE UNREACHABLE CONTACT ADMIN")
    try:
        conn = sql.connect("lite.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM scoreboard ORDER BY score DESC")
        rows = cur.fetchall()
        conn.close()
        return render_template("home.html", rows = rows)
    except:
        return render_template("home.html", no_db = no_db)

@app.route('/launch')
def launch():
    url = ("/zero")
    return render_template('question.html', question = question[0], url = url)

@app.route('/next')
def next():
    url = ("/one")
    return render_template('question.html', question = question[1], url = url)

@app.route('/further')
def further():
    url = ("/two")
    return render_template('question.html', question = question[2], url = url)

@app.route('/almost')
def almost():
    url = ("/three")
    return render_template('question.html', question = question[3], url = url)

@app.route('/last')
def last():
    url = ("/four")
    return render_template('question.html', question = question[4], url = url)

@app.route('/enter')
def enter():
    return render_template('enter.html')

@app.route('/deploy')
def deploy():
    return render_template('deploy.html')

#question ZERO ---------------------------------------------------------------
@app.route('/zero',methods = ['POST', 'GET'])
def zero():
        url = ('next')
        if request.method == 'POST':
            result = request.form
            if request.form['ans'] != answer[0]:
                flash(request.form['ans'] +' is incorrect please try again!')
                return redirect(url_for('launch'))
            else:
                return render_template("result.html", result = result, url = url)

#question ONE ----------------------------------------------------------------
@app.route('/one',methods = ['POST', 'GET'])
def one():
        url = ('further')
        if request.method == 'POST':
            result = request.form
            if request.form['ans'] != answer[1]:
                flash(request.form['ans'] +' is incorrect please try again!')
                return redirect(url_for('next'))
            else:
                return render_template("result.html", result = result, url = url)

#question TWO ----------------------------------------------------------------
@app.route('/two',methods = ['POST', 'GET'])
def two():
        url = ('almost')
        if request.method == 'POST':
            result = request.form
            if request.form['ans'] != answer[2]:
                flash(request.form['ans'] +' is incorrect please try again!')
                return redirect(url_for('further'))
            else:
                return render_template("result.html", result = result, url = url)

#question THREE --------------------------------------------------------------
@app.route('/three',methods = ['POST', 'GET'])
def three():
        url = ('last')
        if request.method == 'POST':
            result = request.form
            if request.form['ans'] != answer[3]:
                flash(request.form['ans'] +' is incorrect please try again!')
                return redirect(url_for('almost'))
            else:
                return render_template("result.html", result = result, url = url)

#question FOUR ---------------------------------------------------------------

@app.route('/four',methods = ['POST', 'GET'])
def four():
        url = ('last')
        if request.method == 'POST':
            result = request.form
            if request.form['ans'] != answer[4]:
                flash(request.form['ans'] +' is incorrect please try again!')
                return redirect(url_for('last'))
            else:
                return render_template("last_result.html", result = result, url = url)

# INSERT DATA INTO DATABASE AND VIEW DATA FROM DATABASE-----------------------
@app.route('/db_insert',methods = ['POST', 'GET'])
def db_insert():
    msg = ("Record NOT added!")
    no_db = ("DATABASE UNREACHABLE!")
    if request.method == 'POST':
        try:
            name = request.form['name']
            score = request.form['score']
            conn=sql.connect("lite.db")
            cur=conn.cursor()
            cur.execute("INSERT INTO scoreboard VALUES (?,?)",(name, score))
            cur.execute("SELECT * FROM scoreboard ORDER BY score DESC")
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            msg = ("Record SUCCESFULLY added!")
            return render_template("home.html", msg = msg, rows = rows)
        except:
            conn.rollback()
            conn.close()
    return render_template("home.html", msg = msg, no_db = no_db)

if __name__ == '__main__':
    app.run(debug = True, port = 80)
