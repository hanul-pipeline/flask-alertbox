from flask import Flask, request
import RPi.GPIO as GPIO


# set app
app = Flask(__name)

# set pins
GREEN_LED_PIN = 17
YELLOW_LED_PIN = 18
RED_LED_PIN = 19
BUZZER_PIN = 27

# set GPIO mode
GPIO.setmode(GPIO.BCM)

# set pins
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# initial settings: GREEN
GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
green_light_on = True


# routers
# /repaired/normal
@app.route('/repaired/normal', methods=['GET'])
def trigger_inspection():
    # turn off
    GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
    GPIO.output(RED_LED_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

    # turn_on
    GPIO.output(GREEN_LED_PIN, GPIO.HIGH)

    return 'triggered'

# /repaired/inspection
@app.route('/repaired/inspection', methods=['GET'])
def trigger_inspection():
    # turn off
    GPIO.output(GREEN_LED_PIN, GPIO.LOW)
    GPIO.output(RED_LED_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

    # turn_on
    GPIO.output(YELLOW_LED_PIN, GPIO.HIGH)

    return 'triggered'

# /alert/inspection
@app.route('/alert/inspection', methods=['GET'])
def trigger_inspection():
    # turn off
    GPIO.output(GREEN_LED_PIN, GPIO.LOW)
    GPIO.output(RED_LED_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

    # turn_on
    GPIO.output(YELLOW_LED_PIN, GPIO.HIGH)

    return 'triggered'

# /alert/evacuation
@app.route('/alert/evacuation', methods=['GET'])
def trigger_inspection():
    # turn off
    GPIO.output(GREEN_LED_PIN, GPIO.LOW)
    GPIO.output(YELLOW_LED_PIN, GPIO.LOW)

    # turn_on
    GPIO.output(RED_LED_PIN, GPIO.HIGH)
    GPIO.output(BUZZER_PIN, GPIO.HIGH)

    return 'triggered'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
