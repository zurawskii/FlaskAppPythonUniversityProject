from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Tytuł posta", validators=[DataRequired()])
    subtitle = StringField("Podtytuł", validators=[DataRequired()])
    img_url = StringField("Zdjęcie URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Zawartość posta", validators=[DataRequired()])
    submit = SubmitField("Opublikuj post")


# Create a form to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Hasło", validators=[DataRequired()])
    name = StringField("Nazwa", validators=[DataRequired()])
    submit = SubmitField("Zarejestruj mnie!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Hasło", validators=[DataRequired()])
    submit = SubmitField("Zaloguj się!")


# Create a form to add comments
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Komentarz", validators=[DataRequired()])
    submit = SubmitField("Opublikuj komentarz")