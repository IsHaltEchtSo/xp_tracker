from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class SkillForm(FlaskForm):
    session_topic   = StringField()
    expose          = IntegerField()
    entry           = IntegerField()
    entry_figure    = IntegerField()
    recap           = IntegerField()
