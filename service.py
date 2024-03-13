from flask import Flask, request, jsonify
import logging

app = Flask("hello_world")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/process_string', methods=['POST'])
def process_string():
    if request.method == 'POST':
        input_string = request.json.get('input_string')  # Extract from JSON
        app.logger.info(f'Received input string: {input_string}')

        if not input_string:
            return jsonify({"error": "Please provide an 'input_string' in the request body"}), 400

        result_string = "Hello World, " + input_string
        return jsonify({"result": result_string})

if __name__ == '__main__':
    app.run(debug=True)