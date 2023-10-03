from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        number = request.form['content']
        if int(number) % 2 == 0:
            return int(number) + ' is even'
        elif int(number) % 2 != 0:
            return int(number) + ' is odd'
        else:
            return number + ' is not an integer'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)