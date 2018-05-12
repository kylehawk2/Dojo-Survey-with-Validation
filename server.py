from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = "keepitsecretkeepitsafe"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def users():
    print "Got post information"
    return redirect('/')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    selected_language = request.form['FavoriteLanguage']
    location=request.form['Dojolocation']
    comment=request.form['description']
    print comment
    if len(request.form['name']) <1:
        flash('Name can not be empty')
        return redirect('/')
    elif len(request.form['description']) <1:
        flash('You need to add a comment')
        return redirect('/')
    elif len (request.form['description']) >=121:
        flash('Comment is larger than 120 characters')
        return redirect('/')
    return render_template("result.html", language=selected_language, location=location, name=name, comment=comment)

app.run(debug=True)