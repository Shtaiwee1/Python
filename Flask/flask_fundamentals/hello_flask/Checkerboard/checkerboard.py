from flask import Flask , render_template
app=Flask(__name__)




# @app.route('/')
# def board(x=4,y=8):
#     return render_template('checkerboard1.html',hor=int(x),ver=int(y))




# @app.route('/<x>')
# def board(x=2,y=8):
#     return render_template('checkerboard2.html',hor=int(x),ver=int(y))




# @app.route('/<x>/<y>')
# def board(x=2,y=8):
#     return render_template('checkerboard2.html',hor=int(x),ver=int(y))


@app.route('/<x>/<y>/<color1>/<color2>')
def board(color1,color2,x=2,y=8,):
    return render_template('checkerboard3.html',hor=int(x),ver=int(y),z=color1,w=color2)









if __name__=="__main__": 
	app.run(debug=True) 