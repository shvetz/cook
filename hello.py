from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/user')
def user():
    return 'This is user page'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'Im a %s' %username

@app.route('/post/<int:post_id>')
def post (post_id):
    return 'This is post number %d' %post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route ('/about')
def about():
    return 'The about page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()