#!/usr/bin/python


# webservice.py
# provides a RESTful API interface to the gensequence function of the fibonacci module


from flask import Flask, jsonify, make_response
import pytest
import fibonacci


app = Flask(__name__)


######################################################################################
# 
# HTTP Root: At the very root URL, let's inform the user how to use the included api(s)
#
######################################################################################
@app.route('/')
def index():
    return "Usage: http://(ip or hostname):(port)/api/v1.0/genfib/(number at or above which to stop the fibonacci sequence)<p>Example:   http://127.0.0.1:8000/api/v1.0/genfib/50000"


######################################################################################
#
# API Endpoint: generate and return a fibonnaci sequence
#
######################################################################################
@app.route('/api/v1.0/genfib/<string:end>', methods=['GET'])
def get_genfib(end):

	# If no input is provided, let's assume this request is from someone who shouldn't be using the api, and let's return a 404 with a "Not Found" message
	if len(end) == 0:
		abort(404)

	# If input is provided, let's check to make sure it's a whole number, and let's return an error message if it's not
	# NOTE: isdigit() is sufficient below, but there's no harm in re-enforcing the input controls
	elif(end.isdigit() == False or float(end)<1 or "." in end): 
		return make_response(jsonify({'error': 'Invalid input. Only natural numbers (whole numbers above 0) are accepted.'}), 400)

	# If this request passed the input checks, let's process the request and give the user their data
	else:
		return make_response(jsonify(fibonacci_sequence = fibonacci.gensequence(int(end))), 200)

		
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
	
	
if __name__ == '__main__':
    app.run(debug=True)
	

	
