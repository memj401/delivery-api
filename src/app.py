from flask import Flask, Blueprint
from rotas import url

app = Flask(__name__)
app.register_blueprint(url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
