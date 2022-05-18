from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields import EmailField
from flask_bootstrap import Bootstrap




class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(min=4)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    email = request.form.get('email')
    password = request.form.get('password')
    if login_form.validate_on_submit():
        if email== 'admin@email.com' and password == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)