from .routes import skill_bp, session
import json
import os
import math


def load_skills_from(path='json/skills.json'):
    with skill_bp.open_resource(path, 'r') as f:
        skills = json.load(f)
    return skills


def dump_skills_to(skills, path='json/skills.json'):
    with open(os.path.join(skill_bp.root_path, path), 'w') as f:
        json.dump(skills, f, indent=2)


def load_xp_rewards(path='json/rewards.json'):
    with skill_bp.open_resource(path, 'r') as f:
        rewards = json.load(f)
        xp_rewards = rewards['xp_rewards']
    return xp_rewards


def calculate_lv(xp):
    if xp == 0:
        return 1

    return math.floor(-1.7 + 1.9*(xp+2) ** 0.5)
