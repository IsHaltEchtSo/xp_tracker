from .routes import skill_bp
from flask import render_template

@skill_bp.app_errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404

@skill_bp.route('/construction')
def construction_page():
    return render_template('zk.html')
