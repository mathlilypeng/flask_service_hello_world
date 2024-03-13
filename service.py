from flask import Flask, request, jsonify
import logging

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
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
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(debug=True)