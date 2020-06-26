
"""index (main) view. URLs include:/."""

from flask import Flask, render_template, flash, redirect
import flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
import arrow
import website

@website.app.route('/')
def show_index():
    """Display / route."""
    platform = flask.request.user_agent.platform
    print(platform)

    title = "Home"
    if platform == 'iphone' or platform == 'android':
        return render_template("index_mobile.html", title = title)
    else:
        return render_template("index.html", title = title)


@website.app.route('/projects')
def show_projects():
    platform = flask.request.user_agent.platform
    print(platform)
    title = "Projects"

    if platform == 'iphone' or platform == 'android':
        return render_template("projects_mobile.html", title = title)
    else:
        return render_template("projects.html", title=title)

@website.app.route('/education')
def show_education():
    platform = flask.request.user_agent.platform
    print(platform)
    title = "Education"

    if platform == 'iphone' or platform == 'android':
        return render_template("education_mobile.html", title = title)
    else:
        return render_template("education.html", title=title)


@website.app.route('/contact', methods=['GET', 'POST'])
def show_contact():
    platform = flask.request.user_agent.platform
    print(platform)

    title = "Contact"
    print('stuff')
    form = ContactForm()

    if form.validate_on_submit():
        print('it worked')

        flash('<b>name:</b> {}'.format(form.name.data))
        flash('email: {}'.format(form.email.data))
        flash('inquiry type: {}'.format(form.inquiry.data))
        flash('message: {}'.format(form.message.data))
        return redirect('/confirmation')
    else:
        print(form.errors)
    if platform == 'iphone' or platform == 'android':


        return render_template("contact_mobile.html", title = title)
    else:


        return render_template("contact.html", title=title, form=form)

@website.app.route('/confirmation')
def show_confirmation():
    platform = flask.request.user_agent.platform
    print(platform)
    title = "Confirmation"

    if platform == 'iphone' or platform == 'android':
        return render_template("confirmation.html", title = title)
    else:
        return render_template("confirmation.html", title=title)


class ContactForm(FlaskForm):
    name = StringField(u'Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    inquiry = SelectField('Inquiry', choices=[('question', 'Question'), ('issue', 'Site Issue'), ('feedback','Feedback'), ('profesional', 'Professional')])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')
