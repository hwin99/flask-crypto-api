from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to receive TradingView alerts
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received alert:", data)  # Debugging

    # Extract trading signal from Pine Script
    trade_signal = data.get("signal")  # "BUY" or "SELL"

    # Simulated AI logic (replace with real AI model later)
    if trade_signal == "BUY":
        response = {"decision": "Executing LONG order"}
    elif trade_signal == "SELL":
        response = {"decision": "Executing SHORT order"}
    else:
        response = {"decision": "No action taken"}

    return jsonify(response)

# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
