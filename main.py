from flask import Flask, render_template

app = Flask(__name__)

@app.route('/calculate&num1=<a>&num2=<b>&operation=<string:c>') //Задаём url по переданным пользователем данным
def calculate(a, b, c):
    if a.isdigit() and b.isdigit(): //Если пользователь ввёл числа, можем выполнять с ними операции
        a = int(a)
        b = int(b)
        if c == "+": //В зависимости от введённой пользователем операции выполняем вычисления
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
                return "<h3>Мы не можем выполнить деление на 0. Введите другие данные</h3>" //Если пользователь ввёл деление на 0, выдаём ошибку
            else:
                h = a / b
                return f'<h3>{a} : {b} = {h}<h3>'
        else:
            return "<h3>Мы не знаем такую операцию<h3>"
    else:
        return "<h3>Мы можем выполнять операции только с числами. Пожалуйста, введите корректные данные<h3>" //Если пользователь ввёл не числовые значения, то выдаём ошибку


if __name__ == '__main__':
    app.run(debug=True)
