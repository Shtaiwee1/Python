from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def create_user():
    if not 'counter' in session:
        session['counter'] = 0
        
    else:
        session['counter'] += 1  
        
    if not 'visits' in session:
        session['visits'] = 0
    else:
        session['visits'] +=1  
    return render_template('counter.html')

@app.route("/destroy_session")
def delete():
    session.clear()
    session['counter']=0
    return redirect('/')

@app.route('/add2')
def add():
    session['counter'] += 1
    return redirect('/')


@app.route('/reset')
def reseter():
    session['counter'] = -1
    return redirect('/')

@app.route('/<x>')
def option(x):
    session['counter'] += int(x)
    return render_template('counter.html',some_num=int(x))











if __name__ == "__main__":
    app.run(debug=True)