from flask import Flask,render_template

'''
creates an instance of Flask,
which will be your WSGI application
'''

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><h1>Welcome learners</h1></html>"

@app.route('/index')
def index():
    # return render_template('index_error.html')  #Note THE ERROR
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

    
if __name__ == '__main__':
    app.run(debug= True) 