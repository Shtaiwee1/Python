
from flask import Flask 
app=Flask(__name__)

@app.route('/')
def hello_world():
    print('hello world')
    return('Hello World!')

@app.route('/Dojo')
def Dojo():
    return 'Dojo'
    
@app.route('/say/<name>')
def say(name):
    return 'Hi' + ' ' + name + '!'

@app.route('/repeat/<num>/<phrase>')
def  repeat(num , phrase):
    if phrase!='hello' and phrase != 'dogs' and phrase != 'bye':
        return 'Sorry! No response. Try again.'
    else:
            for i in range(0,int(num)):
                return  f" {phrase}" * int(num)
    

    


if __name__=="__main__": 
    app.run(debug=True) 