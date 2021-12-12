from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SessionForm(FlaskForm):
    topic   = StringField()
    entry = IntegerField(validators=[validators.optional()])
    entry_figure = IntegerField(validators=[validators.optional()])
    recap = IntegerField(validators=[validators.optional()])
    zettel = IntegerField(validators=[validators.optional()])
    zettel_figure = IntegerField(validators=[validators.optional()])
    konzeptzettel = IntegerField(validators=[validators.optional()])
    konzeptzettel_appendix = IntegerField(validators=[validators.optional()])
    zettel_digitalised = IntegerField(validators=[validators.optional()])
    for_db = IntegerField(validators=[validators.optional()])
    for_db_selfmade = IntegerField(validators=[validators.optional()])
    finished_project = IntegerField(validators=[validators.optional()])
    framework_selfmade = IntegerField(validators=[validators.optional()])
    complete_routine = IntegerField(validators=[validators.optional()])
    routine_part = IntegerField(validators=[validators.optional()])



class SkillForm(FlaskForm):
    skill_name = StringField()
