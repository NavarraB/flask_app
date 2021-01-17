from flask import Flask
from flask import request

app = Flask(__name__)

# http://0.0.0.0:5000/         base url

@app.route('/home')
def index():
    return 'Hello Flask'

@app.route('/users/<user_id>', methods = ['GET', 'DELETE', 'PUT', 'POST'])
def parameter(user_id):
    if request.method == 'GET':

        return 'GET method'

    elif request.method == 'POST':
        data = request.form
        return data

    elif request.method == 'PUT':

        return 'PUT method'

    elif request.method == 'DELETE':

        return 'DELETE method'

    else:
        return 'Not allowed method'

    return user_id

# http://0.0.0.0:5000/users/2
# http://0.0.0.0:5000/users/navarra
# <...> make it dynamic


app.run(host = '0.0.0.0', port = 5000)
