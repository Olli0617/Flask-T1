from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
@app.route('/')
def about():
    return render_template("about.html")


@app.route('/calculate&num1=<a>&num2=<b>&operation=<string:c>')
def calculate(a, b, c):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        if c == "+":
            h = a + b
            return f'<h3>{a} + {b} = {h}<h3>'
        elif c == "-":
            h = a - b
            return f'<h3>{a} - {b} = {h}<h3>'
        elif c == "*":
            h = a * b
            return f'<h3>{a} * {b} = {h}<h3>'
        elif c == ":":
            if b == 0:
                return "<h3>Мы не можем выполнить деление на 0. Введите другие данные</h3>"
            else:
                h = a / b
                return f'<h3>{a} : {b} = {h}<h3>'
        else:
            return "<h3>Мы не знаем такую операцию<h3>"
    else:
        return "<h3>Мы можем выполнять операции только с числами. Пожалуйста, введите корректные данные<h3>"


if __name__ == '__main__':
    app.run(debug=True)