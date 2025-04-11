from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome"


@app.route('/status')
def status():
    return "Server is running"

@app.route('/about')
def about():
    return "This is a simple note-taking web app built with Flask"

if __name__ == '__main__':
    app.run(debug=True)