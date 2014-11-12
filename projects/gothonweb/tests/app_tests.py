from nose.tools import *
from bin.app import app
from test.tools import assert_response

def test_index():
	#check that we got a 404 on the / URL
	resp = app.request("/")
	assert_response(resp, status="404")
	
	#test our first GET requst to /hello
	resp = app.request("/hello")
	assert_response(resp)
	
	#make sure default values work for theform
	resp = app.request("/hello", method="POST")
	assert_response(resp, contains="Nobody")
	
	#test that we got expected values
	data = {'name': 'Zed', 'greet': 'Hola'}
	resp = app.request("/hello", method="POST", data=data)
	assert_response(resp, contains="Zed")