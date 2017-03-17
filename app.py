# -----MODELS AND CONFIG---------

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

import routes


# -----ROUTES---------
from routes.__init__ import *
app.register_blueprint(routes) #enregistrer les routes definies dans le dossier toutes au sein de l'application
								# routes = nom de l'instance de BluePrint dans routes/__init__.py


if __name__ == "__main__":
    app.run(debug=True) 
    db.create_all()
    db.session.commit()
