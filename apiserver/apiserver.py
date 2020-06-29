from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = '2f8ced18-b68c-11ea-9c1a-000c296618b6'

def _fibonacci_list(count):
	lst = [0, 1]
	if count == 1:
		return [0]
	if count == 2:
		return [0, 1]
	count -= 2
	while count > 0:
		lst.append(lst[-2] + lst[-1])
		count -= 1
	return lst

def _factors_list(count):
	return [x for x in range (1, count+1) if count%x==0]

def get_number(n):
	if n is None:
		return None
	try:
		n = int(n)
	except:
		return None
	if n <= 0:
		return None
	return n

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
	count = request.args.get('count')
	count = get_number(count)
	if count is None:
		return "Expected named parameter 'count'", 400
	if count > 100:
		return "count parameter should be < 5000", 400
	return str(_fibonacci_list(count))

@app.route('/factors', methods=['GET'])
def factors():
	count = request.args.get('count')
	count = get_number(count)
	if count is None:
		return "Expected named parameter 'count'", 400
	if count > 1000:
		return "count parameter should be < 5000", 400
	return str(_factors_list(count))

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug = True)
