from flask import Flask, request

app = Flask(__name__)


@app.post("/api/convert-temperature")
def index_post():
    data = request.json
    number = int(data["celsius"])

    answer = dict()
    answer["fahrenheit"] = (9 / 5 * number) + 32

    return (answer, 200, {"content-type": "application-json"})


if __name__ == "__main__":
    app.run(debug=True, port=1234, host="0.0.0.0")
