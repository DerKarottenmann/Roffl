from flask import render_template, Flask
app = Flask(__name__)

Users = {
    'yannik': {
        'name': 'Yannik Dangel',
        'email': 'yannik@example.com'
    }
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/text')
def text():
    return render_template('text.html')


@app.route('/user/<username>')
def user_profile(username):
    # Connect to database
    user = Users.get(username)
    name = user['name']
    email = user['email']

    return render_template('user_profile.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
