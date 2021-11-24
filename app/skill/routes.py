from flask import Blueprint, render_template, url_for, request, redirect, url_for, session
from .forms import SessionForm
import json


skill = Blueprint(
    'skill', __name__, url_prefix='/skills', template_folder='templates'
)

from .errorhandlers import *

@skill.route('/')
@skill.route('/overview/history')
def skills_history_overview():
    with skill.open_resource('json/skills.json', 'r') as f:
        skills = json.load(f)

    return render_template('overview_history.html', skills=skills)



@skill.route('/overview/graph')
def skills_graph_overview():
    return render_template('overview_graph.html', skills=skills)



@skill.route('/<skill>/history', methods=['POST', 'GET'])
def skill_page_historic(skill):
    form = SessionForm(request.form)

    if request.method == 'POST' and form.validate():
        return redirect(url_for('skill.reward_page', skill=form.session_topic.data))

    return render_template('skill-historic.html', skill=skill, form=form)



@skill.route('/<skill>/graph', methods=['POST', 'GET'])
def skill_page_graphical(skill):
    form = SessionForm(request.form)

    if request.method == 'POST' and form.validate():
        return redirect(url_for('skill.reward_page', skill=form.session_topic.data))

    return render_template('skill-graphical.html', skill=skill, form=form)



@skill.route('/<skill>/reward')
def reward_page(skill):
    return render_template('reward.html', skill=skill)
