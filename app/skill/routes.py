from flask import Blueprint, render_template, url_for, request, redirect, url_for
from .forms import SkillForm

skill = Blueprint(
    'skill', __name__, url_prefix='/skills', template_folder='templates'
)


@skill.route('/')
@skill.route('/overview/graph')
def skills_graph_overview():
    return render_template('overview_graph.html')


@skill.route('/overview/history')
def skills_history_overview():
    return render_template('overview_history.html')


@skill.route('/<skill>/history', methods=['POST', 'GET'])
def skill_page_historic(skill):
    form = SkillForm(request.form)

    if request.method == 'POST' and form.validate():
        return redirect(url_for('skill.reward_page', skill=form.session_topic.data))

    return render_template('skill-historic.html', skill=skill, form=form)


@skill.route('/<skill>/graph', methods=['POST', 'GET'])
def skill_page_graphical(skill):
    form = SkillForm(request.form)

    if request.method == 'POST' and form.validate():
        return redirect(url_for('skill.reward_page', skill=form.session_topic.data))

    return render_template('skill-graphical.html', skill=skill, form=form)


@skill.route('/<skill>/reward')
def reward_page(skill):
    return render_template('reward.html', skill=skill)


@skill.app_errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404
