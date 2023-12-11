from flask import Flask
from mongoengine import connect, signals

print('start')

app = Flask(__name__)


connect(host='mongodb+srv://test_user_1:<Password123>@cluster0.3ljam9n.mongodb.net/?retryWrites=true&w=majority')

app.run()


@app.route('/')
def helloWorld():
    return ('hello!')
