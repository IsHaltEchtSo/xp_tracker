from .routes import skill, session
import json


def load_session_skills():
    """check if skills already in session, else load from disc
        then return the skills"""
    try:
        if session['has_skills']:
            skills = session['skills']
            # print('old skills loaded')
    except KeyError:
        with skill.open_resource('json/skills.json', 'r') as f:
            skills = json.load(f)
            session['skills'] = skills
            session['has_skills'] = True
            # print('new skills in session')
    finally:
        return skills


def add_skill_to_session_from(form, skills):
    new_skill = {'name':form.skill_name.data, 'xp':'0', 'lv':'1', 'sessions':[]}
    skills.append(new_skill)
    session['skills'] = skills
