from flask_wtf import FlaskForm
from wtforms import SubmitField


class HunterForm(FlaskForm):
    submit = SubmitField('HUNT')