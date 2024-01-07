from flask import Flask, render_template, request, redirect
import requests
import sqlite3

app = Flask(__name__)

API_KEY = ''  # Replace YOUR_API_KEY with your API key from exchangeratesapi.io

# Create a SQLite database
conn = sqlite3.connect('currency_history.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS history
             (from_currency text, to_currency text, amount real, result real)''')
conn.commit()


@app.route('/')
def index():
    currencies = get_currency_list()
    return render_template('index.html', currencies=currencies)


@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = float(request.form['amount'])

    converted_amount = get_conversion(from_currency, to_currency, amount)

    # Сохраняем результат конвертации в базу данных
    save_to_history(from_currency, to_currency, amount, converted_amount)

    return f"The converted amount is {converted_amount:.2f} {to_currency}"


@app.route('/clear_history')
def clear_history():
    conn = sqlite3.connect('currency_history.db')
    c = conn.cursor()
    c.execute("DELETE FROM history")
    conn.commit()
    conn.close()
    return "History cleared successfully"

@app.route('/history')
def history():
    conn = sqlite3.connect('currency_history.db')
    c = conn.cursor()
    c.execute("SELECT * FROM history")
    history = c.fetchall()
    conn.close()
    return render_template('history.html', history=history)

def get_currency_list():
    url = f'https://open.er-api.com/v6/latest'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        currencies = data['rates'].keys()
        return currencies
    return []


def get_conversion(from_currency, to_currency, amount):
    url = f'https://open.er-api.com/v6/latest'
    params = {'symbols': f"{from_currency},{to_currency}"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        rate_from = data['rates'][from_currency]
        rate_to = data['rates'][to_currency]
        converted_amount = (amount / rate_from) * rate_to
        return converted_amount
    return 0.0


def save_to_history(from_currency, to_currency, amount, result):
    conn = sqlite3.connect('currency_history.db')
    c = conn.cursor()
    c.execute("INSERT INTO history VALUES (?, ?, ?, ?)", (from_currency, to_currency, amount, result))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    app.run(debug=True)
