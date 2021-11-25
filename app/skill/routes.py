from flask import Blueprint, render_template, url_for, request, redirect, url_for, session
from .forms import SessionForm
import json


skill = Blueprint(
    'skill', __name__, url_prefix='/skills', template_folder='templates'
)


from .errorhandlers import *
from .helper_functions import load_session_skills


@skill.route('/')
@skill.route('/overview/history')
def skills_history_overview():
    skills = load_session_skills()
    sessions = []
    for skill_ in skills:
        for session in skill_['sessions']:
            sessions.append(session)

    return render_template('overview_history.html', skills=skills, sessions=sessions)


@skill.route('/<int:skill_index>/history', methods=['POST', 'GET'])
def skill_page_historic(skill_index):
    skills = load_session_skills()
    skill = skills[skill_index]
    sessions = skill['sessions']

    return render_template('skill-historic.html',
        skill=skill,
        skill_index=skill_index,
        sessions=sessions
    )


@skill.route('/<skill>/reward')
def reward_page(skill):
    return render_template('reward.html', skill=skill)
