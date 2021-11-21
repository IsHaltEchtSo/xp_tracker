from flask import Flask
from .skill.routes import skill

app = Flask(__name__)
app.register_blueprint(skill)
