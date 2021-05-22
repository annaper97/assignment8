from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('cv.html')


@app.route('/assignment8')
def assignment8():
    return render_template("assignment8.html", hobbies=['gym', 'tennis', 'travel', 'cooking'])


@app.route('/list')
def list1():
    return render_template('list.html')

@app.route('/assignment9')
def assignment9():
    users_list = [{"firstName": "Michael", "lastName": "Lawson", "Email": "michael.lawson@reqres.in"},
                  {"firstName": "Lindsay", "lastName": "Ferguson", "Email": "indsay.ferguson@reqres.in"},
                  {"firstName": "Tobias", "lastName": "Funke", "Email": "tobias.funke@reqres.in"},
                  {"firstName": "Byron", "Ferguson": "Fields", "Email": "byron.fields@reqres.in"},
                  {"firstName": "George", "lastName": "Edwards", "Email": "george.edwards@reqres.in"},
                  {"firstName": "Rachel", "Ferguson": "Howell", "Email": "rachel.howell@reqres.in"}]
    result = ''

    if 'search' in request.args:
        for user in users_list:
            if request.args['search'] == user['firstName'] \
                    or request.args['search'] == user['lastName'] \
                    or request.args['search'] == user['Email']:

                result = [user['firstName'], user['lastName'], user['Email']]
    else:
        result = ''


if __name__ == '__main__':
    app.run(debug=True)
