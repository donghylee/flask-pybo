from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, TextAreaField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    submit = SubmitField('저장하기')

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목입니다.')])
    submit = SubmitField('답변등록')

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('이름은 필수 입력 항목입니다.'), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired('비밀번호는 필수 입력 항목입니다.'), EqualTo('password2', message='비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired('비밀번호가 일치하지 않습니다.')])
    email = EmailField('이메일', validators=[DataRequired('Email은 필수 입력 항목입니다.'), Email()])
    submit = SubmitField('저장하기')