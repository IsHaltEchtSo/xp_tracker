from flask import Flask
from .skill.routes import skill
from .config import Config

app = Flask(__name__)
app.config.from_object(obj=Config)

app.register_blueprint(skill)
