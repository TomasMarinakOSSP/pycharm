from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/link', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        blog = request.form['blog']
        email = request.form['email']
        radio = request.form['radio']
        return render_template('zkouska.html', blog=blog, email=email, radio=radio)
    return render_template('link.html')



if __name__ == '__main__':
    app.run(debug=True)
