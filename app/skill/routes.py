from flask import Blueprint, render_template, url_for, request, redirect, url_for, session
from .forms import SessionForm, SkillForm
import json


skill = Blueprint(
    'skill', __name__, url_prefix='/skills', template_folder='templates'
)


from .errorhandlers import *
from .helper_functions import load_session_skills, add_skill_to_session_from


@skill.route('/', methods=['POST', 'GET'])
@skill.route('/overview', methods=['POST', 'GET'])
def index():
    form = SkillForm(request.form)
    skills = load_session_skills()
    skill_sessions = []
    for skill_ in skills:
        for skill_session in skill_['sessions']:
            skill_sessions.append(skill_session)

    if request.method == 'POST' and form.validate():
        add_skill_to_session_from(form, skills)
        return redirect(url_for('skill.index'))

    return render_template('index.html',
        form=form,
        skills=skills,
        skill_sessions=skill_sessions
    )



@skill.route('/<int:skill_index>', methods=['POST', 'GET'])
def skill_page(skill_index):
    skills = load_session_skills()
    skill = skills[skill_index]
    skill_sessions = skill['sessions']

    return render_template('skill.html',
        skill=skill,
        skill_index=skill_index,
        skill_sessions=skill_sessions
    )



@skill.route('/<skill>/reward')
def reward_page(skill):
    return render_template('reward.html', skill=skill)
