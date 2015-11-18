from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Length

class MessageForm(Form):
	title = TextField('title', validators=[DataRequired()])
	description = TextField('description', validators=[DataRequired(), Length(max=140)])
