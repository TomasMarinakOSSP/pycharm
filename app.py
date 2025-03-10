from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/link', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        radio = request.form['radio']
        flash("login successful")
        return render_template('zkouska.html', username=username, password=password, radio=radio)
    flash("login failed")
    return render_template('link.html')



if __name__ == '__main__':
    app.run(debug=True)
