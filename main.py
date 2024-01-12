from flask import *

app = Flask(__name__)
app.secret_key = "flask"


@app.route('/')
def home():
    return "Hello World"





if __name__ == '__main__':
    app.run(debug=False)
