
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "6b41fe1498fa4b844d73419d"   # Replace with your API key
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}latest/"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        amount = request.form.get("amount")
        from_currency = request.form.get("from_currency")
        to_currency = request.form.get("to_currency")

        try:
            amount = float(amount)
            response = requests.get(BASE_URL + from_currency)
            data = response.json()

            if data["result"] == "success":
                rate = data["conversion_rates"][to_currency]
                result = round(amount * rate, 2)
            else:
                error = "Error fetching exchange rates."

        except Exception as e:
            error = "Invalid input or API error."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)