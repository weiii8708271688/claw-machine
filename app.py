from flask import Flask, render_template, request, jsonify
import main
import main2
import main3


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    strategy = data['strategy']


    if strategy == 'strategy1':
        # 策略1不需要額外參數
        m = int(data['m'])
        n = int(data['n'])
        x = float(data['x'])
        p = float(data['p'])
        numSimulations = int(data['numSimulations'])
        average_profit, average_scratches = main.run_simulations(m, n, x, p, numSimulations)
    elif strategy == 'strategy2':
        # 策略2不需要額外參數
        m = int(data['m'])
        n1 = int(data['n1'])
        n2 = int(data['n2'])
        x1 = float(data['x1'])
        x2 = float(data['x2'])
        p = float(data['p'])
        numSimulations = int(data['numSimulations'])
        average_profit, average_scratches = main2.run_simulations(m, n1, n2, x1, x2, p, numSimulations)
    elif strategy == 'strategy3':
        m = int(data['m'])
        n = int(data['n'])
        x = float(data['x'])
        p = float(data['p'])
        numSimulations = int(data['numSimulations'])
        average_profit, average_scratches = main.run_simulations(m, n, x, p, numSimulations)
    

    return jsonify({
        'averageProfit': round(average_profit, 2),
        'averageScratches': round(average_scratches, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)