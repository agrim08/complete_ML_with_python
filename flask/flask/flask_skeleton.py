from flask import Flask

'''
creates an instance of Flask,
which will be your WSGI application
'''

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welocme here. Have a good day :)"

@app.route('/index')
def index():
    return "You are at index page :)"

if __name__ == '__main__':
    app.run(debug= True) 