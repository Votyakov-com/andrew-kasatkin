from flask import Flask
from random import shuffle

app = Flask(__name__)


@app.get("/random-quote")
def index():
    with open("quotes.txt", "r", encoding="utf8") as f1:
        data = f1.read().split("\n")
        shuffle(data)
        return data[0]


if __name__ == "__main__":
    app.run(debug=True)
