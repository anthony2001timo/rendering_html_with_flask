from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return'<h1 style="text-align: center">Hellow, world!</h1>' \
          '<p>This is a paragraph.</p>' \
          '<img src=https://media.tenor.com/pWnZhb1cv3QAAAAC/no-pomeranian.gif width=350>'

@app.route("/bye")
def bye():
    return "Bye!"
@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)

greet()
