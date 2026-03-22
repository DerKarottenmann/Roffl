from flask import render_template, Flask
app = Flask(__name__)

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

@app.route('/user/<username>')
def user_profile(username):
    # Connect to database
    user = Users.get(username)
    name = user['name']
    email = user['email']

    return render_template('user_profile.html', name=name, email=email)



if __name__ == '__main__':
    app.run(debug=True)
