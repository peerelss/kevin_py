from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@app.route('/')
def index():
    return render_template('index2.html')


@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        print(data)
        sock.send(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5050)
