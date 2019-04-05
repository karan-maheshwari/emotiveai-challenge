from flask import Flask
from flask import render_template
from twilio.twiml.messaging_response import MessagingResponse
from flask import request
import db_operations
import twilio

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
	actual_keyword, cresponse, iresponse = db_operations.getData(db, metadata)
	result = {'keyword':actual_keyword,'cresponse':cresponse,'iresponse':iresponse}
	return render_template('home.html', result=result)


@app.route("/process", methods=['GET', 'POST'])
def process():
	db_operations.update_keywords(db, metadata, request.form['keyword'], request.form['cresponse'], request.form['iresponse'])
	return 'ok'


@app.route("/sms", methods=['GET', 'POST'])
def receive():
	number = request.form['From']
	keyword = request.form['Body']
	actual_keyword, cresponse, iresponse = db_operations.getData(db, metadata)
	if not db_operations.check_if_contact_is_registered(db, metadata, number):
		msg = MessagingResponse()
		if keyword == actual_keyword:
			msg.message(cresponse)
			db_operations.add_customer(db, metadata, number)
			return str(msg)
		else:
			msg.message(iresponse)
			return str(msg)
	else:
		return "ok"


@app.route("/send_individual", methods=['GET', 'POST'])
def send_individual_message():
	number = request.form['individual_message_phonenumber']
	message = request.form['individual_message_text']
	print(number, message)
	if db_operations.check_if_contact_is_registered(db, metadata, number):
		twilio.send_message(number, message)
	return "ok"


@app.route("/send_blast", methods=['GET', 'POST'])
def send_blast_message():
	message = request.form['blast_message_text']
	contacts = db_operations.get_all_contacts(db, metadata)
	for contact in contacts:
		twilio.send_message(contact[0], message)
	return "ok"


if __name__ == '__main__':
	app.config['DEBUG'] = True
	db, metadata = db_operations.setup()
	app.run()
