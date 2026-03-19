from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/transform', methods=['POST'])
def transform():
    data = request.get_json()

    if not data or 'voltage' not in data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        voltage = float(data['voltage'])
    except:
        return jsonify({"error": "Voltage must be a number"}), 400

    temperature = voltage * 10

    return jsonify({
        "temperature": temperature,
        "unit": "C"
    })

if __name__ == '__main__':
    app.run(debug=True)