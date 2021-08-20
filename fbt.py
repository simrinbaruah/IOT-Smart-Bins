import load
import time

def post_value():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://smartbins-ee107.firebaseio.com/')
    def get_value():
        value = load.load_value()
        print value
        firebase.post('/value', value)

        stop_time = time.time() + 5
        while time.time() < stop_time:
            get_value()
            time.sleep(1)


