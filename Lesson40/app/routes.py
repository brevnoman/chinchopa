from datetime import datetime, date

from flask import jsonify
from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, CreatePostForm
from flask_login import current_user, login_user, login_required
from app.models import User, Posts
from flask import request
from werkzeug.urls import url_parse
from flask_login import logout_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = db.session.query(Posts).order_by(db.desc(Posts.timestamp)).all()
    return render_template("index.html", title='Home Page', posts=posts)


@app.route("/api/posts", methods=["GET"])
def list_posts():
    posts_before = request.args.get("before", "")
    if posts_before:
        posts_before = date.fromisoformat(posts_before)
        posts = Posts.query.filter(Posts.timestamp >= posts_before).all()
    else:
        posts = Posts.query.all()
    posts_list = []
    for post in posts:
        posts_list.append({"body": post.body, "created": post.timestamp})
    return jsonify({"posts": posts_list})


@app.route("/api/posts", methods=["POST"])
def api_create_post():
    data = request.get_json()
    new_post = Posts(body=data.get("body"), user_id=data.get("user_id"))
    db.session.add(new_post)
    try:
        db.session.commit()
    except Exception:
        print("Error!")
        db.session.rollback()
        return jsonify({"status": "Except!"}), 400
    return jsonify({"status": "ok!"})


@app.route('/api/posts/<post_id>', methods=["DELETE"])
def api_delete_post():
    data = request.get_json()
    post = Posts.query.filter_by(post_id=data.get("post_id")).first()
    if not post:
        return jsonify({"status": "ERROR"})
    db.session.delete(post)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"status": "ERROR"})
    return jsonify({"status": "deleted"})



@app.route("/api/posts/<post_id><body>", methods=["PATCH"])
def api_update_post(post_id):
    data = request.get_json()
    post = Posts.query.filter_by(post_id= data.get("post_id")).update({"body": data.get("data")})
    if not post:
        return jsonify({"status": "ERROR"})
    db.session.delete(post)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"status": "ERROR"})
    return jsonify({"status": "deleted"})


@app.route("/api/users", methods=["GET"])
def api_get_users():
    users = User.quary.all()
    return jsonify({"users": users})


@app.route("/api/users/<user_id>", methods=["GET"])
def api_get_user():
    data = request.get_json()
    user = User.quary.filter_by(user_id=data.get("user_id")).first()
    return jsonify({"user": user})


@app.route("/api/users/<user_id><about_me>", methods=["PATCH"])
def api_update_user():
    data = request.get_json()
    user = User.quary.filter_by(user_id=data.get("user_id")).update({"about_me": data.get("about_me")})
    if not user:
        return jsonify({"status": "ERROR"})
    db.session.add(user)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"status": "ERROR"})
    return jsonify({"status": "changed"})


@app.route("/api/users/<user_id>", methods=["DELETE"])
def api_delete_user():
    data = request.get_json()
    user = User.quary.filter_by(user_id=data.get("user_id")).first()
    if not user:
        return jsonify({"status": "ERROR"})
    db.session.delete(user)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"status": "ERROR"})
    return jsonify({"status": "user deleted"})


@app.route("/api/register/<username><email><password>", methods=["POST"])
def api_register():
    data = request.get_json()
    user = User(username=data.get("username"), email=data.get("email"))
    if not user:
        return jsonify({"status": "ERROR"})
    user.set_password(data.get("password"))
    db.session.add(user)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"status": "ERROR"})
    return jsonify({"status": "user created"})


@app.route("/api/login/<username><password><remember_me>", methods=["POST"])
def api_user_login():
    data = request.get_json()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        user = User.query.filter_by(username=data.get("username")).first()
        if user is None or not user.check_password(data.get("password")):
            return jsonify({"status": "wrong username or password"})
        login_user(user, remember=bool(data.get("remember_me")))
    return jsonify({"status": "Login successfully"})


@app.route('/dinah')
def idi_nahuy():
    return render_template("dinah.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(db.desc(Posts.timestamp))
    return render_template('user.html', user=user, posts=posts)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

@app.route("/create_new_post", methods=["GET", "POST"])
@login_required
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post_body = form.post.data
        post = Posts(body=post_body, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('user', username=current_user.username))
    return render_template("create_post.html", form=form)


@app.route("/delete_post/<post_id>&<post_body>", methods=["GET", "POST"])
@login_required
def delete_post(post_id, post_body):
    post = db.session.query(Posts).filter(Posts.id==post_id, Posts.body==post_body).first()
    print(post)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('user', username=current_user.username))