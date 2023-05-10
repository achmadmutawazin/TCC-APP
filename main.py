from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 + num2  # Perform the calculation (you can replace it with any desired calculation)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run()
