from wtforms import Form, StringField, IntegerField

class SkillForm(Form):
    session_topic   = StringField()
    expose          = IntegerField()
    entry           = IntegerField()
    entry_figure    = IntegerField()
    recap           = IntegerField()
