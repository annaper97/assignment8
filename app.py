from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('cv.html')


@app.route('/assignment8')
def assignment8():
    return render_template("assignment8.html", hobbies=['gim', 'tennis', 'travel', 'cooking'])


@app.route('/list')
def list1():
    return render_template('list.html')



if __name__ == '__main__':
    app.run(debug=True)

