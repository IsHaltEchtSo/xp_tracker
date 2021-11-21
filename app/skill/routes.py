from flask import Blueprint, render_template, url_for

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


@skill.route('/<skill>/history')
def skill_page_historic(skill):
    return render_template('skill-historic.html', skill=skill)


@skill.route('/<skill>/graph')
def skill_page_graphical(skill):
    return render_template('skill-graphical.html', skill=skill)


@skill.route('/<skill>/reward')
def reward_page(skill):
    return render_template('reward.html', skill=skill)
