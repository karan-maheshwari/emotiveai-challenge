from twilio.rest import Client


def send_message(number, message):
    account_sid = 'insert_from_instructions_file'
    auth_token = 'insert_from_instructions_file'
    client = Client(account_sid, auth_token)

    sent_message = client.messages \
                    .create(
                         body=message,
                         from_='+19495180268',
                         to=number
                     )

    print(sent_message.sid)
