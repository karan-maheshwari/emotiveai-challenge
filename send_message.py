from twilio.rest import Client


def send_message(number, message):
    account_sid = 'ACc5f8cde7803bf03ccb12a7036e234b6d'
    auth_token = 'fc09aa101d3da202666f256fd6489fb6'
    client = Client(account_sid, auth_token)

    sent_message = client.messages \
                    .create(
                         body=message,
                         from_='+19495180268',
                         to=number
                     )

    print(sent_message.sid)
