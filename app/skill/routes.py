from flask import Blueprint, render_template, url_for, request, redirect, url_for, session
from .forms import SessionForm, SkillForm
import json


skill = Blueprint(
    'skill', __name__, url_prefix='/skills', template_folder='templates'
)


from .errorhandlers import *
from .helper_functions import (
     load_skills_from, dump_skills_to
)


@skill.route('/', methods=['POST', 'GET'])
@skill.route('/overview', methods=['POST', 'GET'])
def index():
    form = SkillForm(request.form)
    skills = load_skills_from(path='json/skills.json')
    skill_sessions = []

    for skill_name, skill_props in skills.items():
        for skill_session in skill_props['sessions']:
            skill_sessions.append(skill_session)

    if request.method == 'POST' and form.validate():
        new_skill_name = form.skill_name.data
        new_skill = {'name':new_skill_name, 'xp':'0', 'lv':'1', 'sessions':[]}
        skills[new_skill_name] = new_skill
        dump_skills_to('json/skills.json', skills)
        return redirect(url_for('skill.index'))

    return render_template('index.html',
        form=form,
        skills=skills,
        skill_sessions=skill_sessions
    )



@skill.route('/<skill_name>', methods=['POST', 'GET'])
def skill_page(skill_name):
    form = SessionForm(request.form)
    skills = load_skills_from(path='json/skills.json')
    # skill_ = skills[skill_index]
    skill_sessions = skills[skill_name]['sessions']

    if request.method == 'POST' and form.validate():
        new_session = {
            'date':'11.11.11','xp':'20','topic':'gangsters in paradise','mediums':[]
        }
        skill_sessions.append(new_session)
        # skill_['sessions'] = skill_sessions
        skills[skill_name]['sessions'] = skill_sessions

        dump_skills_to(path='json/skills.json', skills=skills)
        return redirect(url_for('skill.reward_page', skill=skill_name))

    return render_template('skill.html',
        skill=skills[skill_name],
        skill_name=skill_name,
        skill_sessions=skill_sessions,
        form=form
    )



@skill.route('/<skill>/reward')
def reward_page(skill):
    return render_template('reward.html', skill=skill)
