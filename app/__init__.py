from flask import Flask
from .blueprints.skill.routes import skill_bp
from .config import Config

app = Flask(__name__)
app.config.from_object(obj=Config)

app.register_blueprint(skill_bp)
