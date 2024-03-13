from flask import Flask, request, jsonify

app = Flask("hello_world")

@app.route('/process_string', methods=['POST'])
def process_string():
    if request.method == 'POST':
        input_string = request.json.get('input_string')  # Extract from JSON

        if not input_string:
            return jsonify({"error": "Please provide an 'input_string' in the request body"}), 400

        result_string = "Hello World, " + input_string
        return jsonify({"result": result_string})

if __name__ == '__main__':
    app.run(debug=True)