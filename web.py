# source du script sur http://flask.pocoo.org/
# Attention de de pas oublier de metre le chemin des executable de python comme sur la ligne 3 ci-dessous
#!/usr/bin/python3
from flask import Flask, redirect, url_for
# construction d'un objet (applicatif)
app = Flask(__name__)

@app.route("/")
def hello(): #fonction
    return redirect(url_for('test'))

@app.route("/test")
def test():
    return "<h1>Hello le redirect</h1>"

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello %s</h1>" % name

if __name__ == "__main__":
    app.run(debug=True)
