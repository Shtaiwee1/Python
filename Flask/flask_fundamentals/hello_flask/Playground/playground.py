from flask import Flask , render_template
app=Flask(__name__)

# @app.route('/play')
# def repeat():
#     return render_template("playground_level_1.html")




# @app.route('/play/<num>')
# def repeat(num):
#     return render_template("playground_level_2.html",some_num=int(num))




@app.route('/play/<num>/<color>')
def repeat(num,color):
    return render_template("playground_level_3.html",some_num=int(num),some_color=color)






if __name__=="__main__": 
		app.run(debug=True) 
