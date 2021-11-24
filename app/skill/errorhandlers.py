from .routes import skill
from flask import render_template

@skill.app_errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404
