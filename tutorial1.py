from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "This is the main page <h1>Hi!</h1>"

if __name__ == "__main__":
    app.run()