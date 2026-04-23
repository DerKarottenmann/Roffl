from flask import render_template, Flask, request, url_for, redirect, session, flash, Response
from models import db, Entry, Image
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
import dotenv
import os
import time
import json

dotenv.load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.secret_key = os.getenv("SKEY")
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def Mainpage():
    entries = Entry.query.order_by(Entry.created_at.desc()).limit(10).all()
    return render_template('index.html', entries=entries, title="Mainpage")

@app.route('/description')
def description():
    return render_template('description.html', title="Description")

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if len(request.form['text']) < 25:
            flash("Text must be at least 25 characters long.")
            return redirect(url_for('create'))
        title = request.form['title']
        text = request.form['text']
        images = request.files.getlist('images')
        user_id = session.get("user_id")

        new_entry = Entry(title=title, text=text, owner=user_id, created_at=db.func.now())
        db.session.add(new_entry)
        db.session.flush()  # new_entry.id bekommen

        if images and len(images) > 0:
            for image in images:
                new_image = Image(data=image.read(), entry_id=new_entry.id)
                db.session.add(new_image)

        db.session.commit()

        return redirect(url_for('Mainpage'))

    return render_template('create.html', title="Create New Entry")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Passwort hashen
        hashed_password = generate_password_hash(password)

        # User erstellen
        new_user = User(
            username=username,
            email=email,
            password_hash=hashed_password
        )

        # Datenbank speichern
        db.session.add(new_user)
        db.session.commit()

        return "Signup successful! User saved to database."

    return render_template('signup.html', title="Signup")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # User aus db
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            session.clear()
            session["user_id"] = user.id
            session["username"] = user.username
            session["logged_in"] = True
            return redirect(url_for('Mainpage'))
        else:
            return "Invalid username or password."

    return render_template('login.html', title="Login")


@app.route('/logout')
def logout():
    session.clear()
    return render_template('logout.html', title="Logout")


@app.route('/image/<int:image_id>')
def get_image(image_id):
    image = Image.query.get_or_404(image_id)
    return image.data, 200, {'Content-Type': 'image/jpeg'}

@app.route('/statistics')
def statistics():
    return render_template('statistics.html', title="Statistics")


@app.route('/stream')
def stream():
    print("SSE: generating data...")
    def generate():
        with app.app_context():
            entry = Entry.query.order_by(Entry.id.desc()).limit(1).first()
            if entry is None:
                last_id = 0
            else:
                last_id = entry.id
            while True:
                db.session.expire_all()
                dic = []
                entries = Entry.query.filter(Entry.id > last_id).order_by(Entry.created_at.desc()).limit(15).all()
                if entries:
                    last_id = max(entries, key=lambda e: e.id).id
                    for entry in entries:
                        dic.append({"Titel": entry.title, "Text": entry.text})
                    sse_data = json.dumps(dic)
                    yield f"data: {sse_data}\n\n"
                time.sleep(1)

    return Response(generate(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True)
