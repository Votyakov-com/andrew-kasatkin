from flask import Flask, request, redirect
import json

app = Flask(__name__)

# Первая реализация программы.
# Пытался отправить из return`a функции index_get данные в виде JSON, но реализовать не получилось.
# Это вообще возможно?


@app.get("/api/convert-temperature")
def index_get():
    return f"""
    <form method="POST" action="/api/convert-temperature">
    <fieldset>
    <legend>Temperature Conversion Calculator: <i>Celsius</i> to <i>Fahrenheit</i></legend>
    <br>
    <input name="value" placeholder="Enter temperature in ℃">
    <br><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <button type="submit" style='color:blue'>Submit</button>
    </fieldset>
    </form>
    """


@app.post("/api/convert-temperature")
def index_post():
    response = request.form.get("value")
    answer = (9 / 5 * int(response)) + 32
    return f"<h4>Temperature in fahrenheit is: {str(answer)}℉</h4>"


if __name__ == "__main__":
    app.run(debug=True)
