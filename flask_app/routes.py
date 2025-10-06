from flask_app.models import User, Course, Lesson
from flask import redirect, render_template,flash, url_for
from flask_app.forms import RegistrationForm, LoginForm
from flask_app import app, db, bc
from flask_login import login_user, current_user,logout_user, login_required
''

lessons = [
    {
        "title": "Python for Beginners",
        "course": "Python",
        "author": "Salima Dergoul",
        "thumbnail": "python1.jpg",
    },
    {
        "title": "Advanced Python Projects",
        "course": "Python",
        "author": "Salima Dergoul",
        "thumbnail": "python2.jpeg",
    },
    {
        "title": "Python Automation Essentials",
        "course": "Python",
        "author": "Salima Dergoul",
        "thumbnail": "python3.jpg",
    },
    {
        "title": "Java Fundamentals",
        "course": "Java",
        "author": "Badr Ouaddah",
        "thumbnail": "java1.jpg",
    },
    {
        "title": "Java OOP Mastery",
        "course": "Java",
        "author": "Badr Ouaddah",
        "thumbnail": "java2.jpg",
    },
    {
        "title": "Building Java Applications",
        "course": "Java",
        "author": "Badr Ouaddah",
        "thumbnail": "java3.jpg",
    },
]
courses = [
    {
        "name": "Python",
        "icon": "python.jpg",
        "description": "Master Python from basics to advanced projects with hands-on lessons and real-world examples.",
    },
    {
        "name": "Java",
        "icon": "java.jpg",
        "description": "Learn Java fundamentals, object-oriented programming, and build scalable applications.",
    },
    {
        "name": "Data Analysis",
        "icon": "analysis.jpg",
        "description": "Explore data analysis techniques using Python, Excel, and visualization tools.",
    },
    {
        "name": "Machine Learning",
        "icon": "machine_learning.jpg",
        "description": "Dive into machine learning algorithms and build intelligent systems with Python.",
    },
    {
        "name": "Web Design",
        "icon": "web.jpg",
        "description": "Design beautiful, responsive websites using HTML, CSS, and modern frameworks.",
    },
    {
        "name": "Tips & Tricks",
        "icon": "idea.jpg",
        "description": "Discover developer hacks, productivity tips, and coding shortcuts to level up your workflow.",
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "home.html", lessons=lessons, courses=courses, title="flask Home page"
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pass=bc.generate_password_hash(form.password.data).decode("utf-8")
        db.session.add(User(fname=form.fname.data, lname=form.lname.data, username=form.username.data, email=form.email.data, password=hash_pass))
        db.session.commit()
        flash(f"Successfully account created for {form.username.data}", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Registration Page", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user= User.query.filter_by(email= form.email.data).first()
        if user and bc.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("You have already signed in!", "success")
            return redirect(url_for("home"))
        else:
            flash("login unsuccessfull, please check credentails", "danger")
    return render_template("login.html", title="Login Page", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/learn", methods=["GET", "POST"])
def learn():
    return "<h1>learning page </h1>"


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

