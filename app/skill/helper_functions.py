from .routes import skill, session
import json
import os


def load_skills_from(path='json/skills.json'):
    with skill.open_resource(path, 'r') as f:
        skills = json.load(f)
    return skills


def dump_skills_to(path, skills):
    with open(os.path.join(skill.root_path, path), 'w') as f:
        json.dump(skills, f, indent=2)
