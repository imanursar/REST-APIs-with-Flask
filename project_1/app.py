from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET']) #https://www.google.com/
def home():
    return ("Hello world !!!!")

app.run(port=5000,debug=True)
