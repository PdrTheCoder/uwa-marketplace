from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, SelectField, DecimalField
from wtforms.validators import DataRequired


class PublishForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": "Add your product title briefly"})
    price = DecimalField('Price', validators=[DataRequired()], render_kw={"placeholder": "Add price"})
    condition = SelectField('Condition', choices=[
        (0, 'New'),
        (1, 'Used - Like New'),
        (2, 'Used - Good'),
        (3, 'Used - Fair')
    ], validators=[DataRequired()])
    photo = FileField(validators=[FileRequired(),
                                  FileAllowed(['jpg', 'png'], 'Images only!')])
    description = TextAreaField('Description',
                                validators=[DataRequired()],
                                render_kw={ "placeholder": "Provide information including color, brand, size, type, any imperfections and so on..."})


class MessageForm(FlaskForm):
    messageContent = TextAreaField('messageContent', validators=[DataRequired()])
