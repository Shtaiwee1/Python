from flask import Flask, render_template, request 
app = Flask(__name__)


@app.route('/')
def form():
    return render_template('dojo_survey.html')



@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    fav_from_form = request.form['fav']
    comment_from_form = request.form['comment']
    checkbox_from_form=request.form['d_enabled']

    return render_template("show.html", name_on_template=name_from_form, location_on_template=location_from_form,
                           fav_on_template=fav_from_form,comment_on_template=comment_from_form,checkbox_on_template= checkbox_from_form)








if __name__ == "__main__":
    app.run(debug=True)