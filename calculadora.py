from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        if operation == 'add':
            result = num1 + num2
            return render_template('index.html', result=result)
        elif operation == 'subtract':
            result = num1 - num2
            return render_template('index.html', result=result)
        elif operation == 'multiply':
            result = num1 * num2
            return render_template('index.html', result=result)
        elif operation == 'divide':
            result = num1 / num2
            return render_template('index.html', result=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
