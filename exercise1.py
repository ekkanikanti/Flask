from flask import Flask, render_template
from datetime import date, datetime

app = Flask(__name__)

@app.route('/')
def index():
    dt = datetime.now().strftime("%A, %B %d %Y %H:%M:%S")

    results = {'datetime' : dt}
    return render_template('dates.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)