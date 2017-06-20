from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/', methods=['GET'])
def index():
    session['jackpot'] = random.randrange(1, 101)
    print 'correct number is', session['jackpot']
    return render_template('index.html')

@app.route('/', methods=['POST'])
def guess():
    guess = request.form['guess']
    print 'guess is', int(guess)
    print 'correct number is', session['jackpot']
    if int(guess) == int(session['jackpot']):
        session.pop('jackpot')
        return render_template("correct.html", guess=guess)
    elif int(guess) < int(session['jackpot']):
        return render_template("low.html")
    elif int(guess) > int(session['jackpot']):
        return render_template("high.html")

app.run(debug=True)
