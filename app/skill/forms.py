from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SessionForm(FlaskForm):
    session_topic   = StringField()
    entry = StringField(validators=[validators.optional()])
    entry_figure = StringField(validators=[validators.optional()])
    recap = StringField(validators=[validators.optional()])
    zettel = StringField(validators=[validators.optional()])
    zettel_figure = StringField(validators=[validators.optional()])
    konzeptzettel = StringField(validators=[validators.optional()])
    konzeptzettel_appendix = StringField(validators=[validators.optional()])
    zettel_digitalised = StringField(validators=[validators.optional()])
    for_db = StringField(validators=[validators.optional()])
    for_db_selfmade = StringField(validators=[validators.optional()])
    finished_project = StringField(validators=[validators.optional()])
    framework_selfmade = StringField(validators=[validators.optional()])
    complete_routine = StringField(validators=[validators.optional()])
    routine_part = StringField(validators=[validators.optional()])



class SkillForm(FlaskForm):
    skill_name = StringField()
