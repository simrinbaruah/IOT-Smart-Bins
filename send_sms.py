import time
from sinchsms import SinchSMS
def sms():
    number = '+918638590897'
    message = 'Dustbin is Full!'

    client = SinchSMS('1fcdbf4e-877e-4182-a7b1-bbffff5084c1', 'Yd6v1yvwukmmjnect0tH6A==')

    print("Sending '%s' to %s" % (message, number))
    response = client.send_message(number, message)
    message_id = response['messageId']

