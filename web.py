# source du script sur http://flask.pocoo.org/
# Attention de de pas oublier de metre le chemin des executable de python comme sur la ligne 3 ci-dessous
#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()