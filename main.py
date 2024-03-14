from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')
  
@app.route('/calculate', methods=['GET'])
def calculate():
    # Extract numbers and operation from query parameters
    num1 = request.args.get('num1', default=0, type=float)
    num2 = request.args.get('num2', default=0, type=float)
    operation = request.args.get('operation', default='add', type=str)

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    else:
        return "Invalid operation."

    return f"The result is {result}"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
