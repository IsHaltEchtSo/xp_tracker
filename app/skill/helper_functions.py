from .routes import skill_bp, session
import json
import os


def load_skills_from(path='json/skills.json'):
    with skill_bp.open_resource(path, 'r') as f:
        skills = json.load(f)
    return skills


def dump_skills_to(path, skills):
    with open(os.path.join(skill_bp.root_path, path), 'w') as f:
        json.dump(skills, f, indent=2)
