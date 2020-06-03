# YOUR FLASK APP HERE
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    # return 'hello world'
    return render_template('home.html')

@app.route('/loops')
def loops():
    return render_template('loops.html')

@app.route('/operators')
def operators():
    if request.method == 'GET':
        return render_template('operators.html')
    elif request.method == 'POST':
        db.operators.insert_one({
            'name': request.form['name'],
            'description': request.form['description'],
            'symbol': request.form['symbol'],
        })
        return redirect('/operators') 

if __name__ == "__main__":
    app.run()
