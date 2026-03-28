from flask import render_template, Flask, request, url_for, redirect
from models import db
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
migrate = Migrate(app, db)


Users = {
    'yannik': {
        'name': 'Ben Jahu ',
        'email': 'jahu@example.com'
    }
}

@app.route('/')
def Mainpage():
    return render_template('index.html')

@app.route('/description')
def description():
    return render_template('description.html')

@app.route('/create')
def create():
    return render_template('create.html')

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

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # User aus db
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            return "Login successful!"
        else:
            return "Invalid username or password."

    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)
