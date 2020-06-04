
"""index (main) view. URLs include:/."""

from flask import Flask, render_template
import flask
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


@website.app.route('/contact')
def show_contact():
    platform = flask.request.user_agent.platform
    print(platform)

    title = "Contact"

    if platform == 'iphone' or platform == 'android':
        return render_template("contact_mobile.html", title = title)
    else:
        return render_template("contact.html", title=title)
