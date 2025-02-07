from flask import Flask, request, jsonify
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

def is_armstrong(n):
	digits = [int(d) for d in str(n)]
	return sum(d ** len(digits) for d in digits) == n

def is_perfect(n):
	return n == sum(i for i in range(1, n) if n % 1 == 0)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
	number = request.args.get('number')

	# validate input (handles negatives and non-integer values)
	try:
		num = int(number)
	except ValueError:
		return jsonify({"number": number, "error": True}), 400
	
	properties = ["odd" if num % 2 else "even"]

	if is_armstrong(num):
		properties.insert(0, "armstrong")

	# Get fun fact
	fact_url = f"http://numbersapi.com/{num}/math"
	fun_fact = requests.get(fact_url).text

	response = {
		"number": num,
		"is_prime": is_prime(num),
		"is_perfect": False,
		"properties": properties,
		"digit_sum": sum(int(d) for d in str(num)),
		"fun_fact": fun_fact
	
	}
	return jsonify(response), 200

if __name__ == '__main__':
	app.run(debug=True)
