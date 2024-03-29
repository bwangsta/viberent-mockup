from mockup import app
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us")

@app.route("/story")
def story():
    return render_template("story.html", title="Our Story")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Us")