from flask import render_template, Flask, request
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


@app.route('/user/<username>')
def user_profile(username):
    # Connect to database
    user = Users.get(username)
    name = user['name']
    email = user['email']

    return render_template('user_profile.html', name=name, email=email)



if __name__ == '__main__':
    app.run(debug=True)
