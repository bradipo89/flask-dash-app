from flask import Blueprint, render_template, redirect, url_for,request
from flask_login import login_user, login_required, logout_user
from myapp.home.models import User
from myapp.home.forms import LoginForm, RegistrationForm
from myapp import  db
from flask import flash





bp_home = Blueprint('main', __name__)
bp_logout = Blueprint('main2', __name__)
bp_login = Blueprint('main3', __name__)
bp_regist = Blueprint('main4', __name__)


@bp_home.route("/")
def index():
    return render_template('home.html')


@bp_logout.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out")
    return redirect(url_for('main.index'))

@bp_login.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Logged in Successfully')

            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('main.index')

            return redirect(next)

    return render_template('login.html', form = form)


@bp_regist.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration')
        return redirect(url_for('main.index'))
    return render_template('register.html', form = form)