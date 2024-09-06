# Building  dynamic urls
# Variable Rule
# Jinja Template

'''
{{ }} expressions to print o/p in html
{%...%} conditions-loops
{#...#} single line comments

'''

from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><h1>Welcome learners</h1></html>"

@app.route('/index',methods = ['GET'])
def index():
    return render_template('index.html')

#Variable Rule:
@app.route('/success/<int:score>')  #by default it is string
def success(score):
    res= ''
    if score >= 40:
        res = 'PASS'
    else:
        res = 'FAIL'
    return render_template('result.html',result = res)

#for condition
@app.route('/successres/<int:score>') 
def successres(score):
    res= ''
    if score >= 40:
        res = 'PASS'
    else:
        res = 'FAIL'
    
    exp = {'score':score,'res':res}
    
    return render_template('result1.html',result = exp)

#if condition
@app.route('/scoreif/<int:score>') 
def successif(score):
        
    return render_template('result2.html',result = score)

#dynamic urls:
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',result = score)

@app.route('/submit',methods = ['GET','POST'])
def submit():
    total = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total = (science + maths + c + data_science) / 4
        
    else:
        return render_template('getres.html')
    
    return redirect(url_for('successres' , score = total))

if __name__ == '__main__':
    app.run(debug= True)  