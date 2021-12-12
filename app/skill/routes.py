from flask import Blueprint, render_template, url_for, request, redirect, url_for, session
from .forms import SessionForm, SkillForm
import json
from datetime import date


skill_bp = Blueprint(
    'skill_bp', __name__, url_prefix='/skills', template_folder='templates'
)


from .errorhandlers import *
from .helper_functions import (
     load_skills_from, dump_skills_to, load_xp_rewards, calculate_lv
)


@skill_bp.route('/', methods=['POST', 'GET'])
@skill_bp.route('/overview', methods=['POST', 'GET'])
def index():
    form = SkillForm(request.form)
    skills = load_skills_from(path='json/skills.json')
    skill_sessions = []

    # load all sessions from all skills
    for skill in skills.values():
        for skill_session in skill['sessions']:
            skill_sessions.append(skill_session)

    # process form and update skills
    if request.method == 'POST' and form.validate():
        # init new skill
        new_skill_name = form.skill_name.data
        new_skill = {'name':new_skill_name, 'xp':0, 'lv':'1', 'sessions':[]}
        # add to skills and save as json
        skills[new_skill_name] = new_skill
        dump_skills_to(path='json/skills.json', skills=skills)

        return redirect(url_for('skill_bp.index'))

    return render_template('index.html',
        form=form,
        skills=skills,
        skill_sessions=skill_sessions
    )



@skill_bp.route('/<skill_name>', methods=['POST', 'GET'])
def skill_page(skill_name):
    form = SessionForm(request.form)
    skills = load_skills_from(path='json/skills.json')
    skill = skills[skill_name]

    if request.method == 'POST' and form.validate():
        xp_rewards = load_xp_rewards()
        new_session = {
             'date':str(date.today()),
             'xp':0,
             'mediums':[]
        }
        populated_medium_fields = {}

        # filter medium fields for later use
        # use topic field as the session's topic
        for field in form:
            if field.widget.input_type != 'hidden':
                if field.name != 'topic' and field.data:
                    populated_medium_fields[field.name] = field.data
                elif field.name == 'topic':
                    new_session['topic'] = field.data

        # process the session's mediums
        for medium_name, medium_value in populated_medium_fields.items():
            new_medium = {
                'medium': medium_name,
                'amount': medium_value,
                'xp': xp_rewards[medium_name] * medium_value
            }
            new_session['mediums'].append(new_medium)
            new_session['xp'] += new_medium['xp']

        # append session to skill and update xp/lv of the skill
        skill['sessions'].append(new_session)
        skill['xp'] += new_session['xp']
        skill['lv'] = calculate_lv(skill['xp'])

        dump_skills_to(path='json/skills.json', skills=skills)
        return redirect(url_for('skill_bp.reward_page', skill=skill_name))

    return render_template('skill.html',
        skill=skill,
        skill_name=skill_name,
        skill_sessions=skill['sessions'],
        form=form
    )



@skill_bp.route('/<skill>/reward')
def reward_page(skill):
    return render_template('reward.html', skill=skill)



@skill_bp.route('xp-rewards')
def xp_rewards():
    xp_dict = load_xp_rewards()
    return render_template('xp-rewards.html', xp_dict=xp_dict)
