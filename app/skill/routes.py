from flask import Blueprint

skill = Blueprint('skill', __name__, url_prefix='/skills')


@skill.route('/')
@skill.route('/overview')
def skills_overview():
    return 'the skills'


@skill.route('/skill/<skill>')
def skill_page(skill):
    return 'the page for the {} skill'.format(skill)


@skill.route('/reward')
def reward_page():
    return 'pick your reward'
