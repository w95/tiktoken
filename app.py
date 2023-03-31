from flask import Flask, request, jsonify, make_response
from functions import num_tokens_from_messages

app = Flask(__name__)

@app.route('/')
def root():
	return 'Tiktoken - Token counter'

@app.route('/count', methods=['POST'])
def count():
	try:
		req = request.json
	except Exception as e:
		return make_response(jsonify({
			'error': str(e)
		}), 400)

	return {
		"count": num_tokens_from_messages(req['messages'], req['model'])
	}

if __name__ == "__main__":
	app.run()