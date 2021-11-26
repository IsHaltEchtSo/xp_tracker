from .routes import skill, session
import json
import os


def load_skills_from_bp(path):
    with skill.open_resource(path, 'r') as f:
        skills = json.load(f)
    return skills


def load_session_skills():
    """check if skills already in session, else load from disc
        then return the skills"""
    try:
        if session['has_skills']:
            skills = session['skills']
            # print('old skills loaded')
    except KeyError:
        skills  = load_skills_from_bp(path='json/skills.json')
        session['skills'] = skills
        session['has_skills'] = True
        # print('new skills in session')
    finally:
        return skills


def add_skill_to_session_from(form):
    skills = load_session_skills()
    new_skill = {'name':form.skill_name.data, 'xp':'0', 'lv':'1', 'sessions':[]}
    skills.append(new_skill)
    session['skills'] = skills


def dump_skills_from_bp_to(path):
    skills = session['skills']
    with open(os.path.join(skill.root_path, path), 'w') as f:
        json.dump(skills, f, indent=2)
