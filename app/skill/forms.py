from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SessionForm(FlaskForm):
    session_topic   = StringField()
    expose          = IntegerField(validators=[validators.optional()])
    entry           = IntegerField(validators=[validators.optional()])
    entry_figure    = IntegerField(validators=[validators.optional()])
    recap           = IntegerField(validators=[validators.optional()])

class SkillForm(FlaskForm):
    skill_name = StringField()
