from flask import Flask
from flask_ask import Ask, statement, question
import boto3
import logging

s3 = boto3.resource('s3')

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)



@ask.launch
def launch():
	#welcome_msg = render_template('welcome')
	return question('Welcome. Schoology is now open. What day would you like to learn more about?')
	
	
@ask.intent("DayIntent")
def assignment(dayofweek):
	z = dayofweek.upper()
	logging.getLogger("flask_ask").debug("dayofweek=%s", z )
	if z == 'MONDAY' or z == 'TUESDAY' or z == 'WEDNESDAY' or z == 'THURSDAY' or z == 'FRIDAY' or z == 'SATURDAY' or z == 'SUNDAY':
		try:
			s3.Object('pds-assignments', z).load()
		except Exception as e:
		    if e.response['Error']['Code'] == "404":
				a = 'There is no information for this date'
		else:
			obj = s3.Object('pds-assignments', z).get()
			a = obj['Body'].read()
	else:
		# print('test')
		a = 'That is not a valid day'
		
	return question(a)
	
@ask.intent("StopIntent")
def stop():
	return statement('Thanks for using schoology. Bye-bye.')
	
if __name__ == 'main':
	app.run(debug=True)	
	
