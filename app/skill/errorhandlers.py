from .routes import skill
from flask import render_template

@skill.app_errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404

@skill.route('/zk')
def construction_page():
    return render_template('zk.html')
