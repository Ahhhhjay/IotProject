from flask import Flask, request, jsonify,render_template
import RPi.GPIO as GPIO

# Set up Flask app
app = Flask(__name__)

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
LED_PIN = 26  
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  


led_on = False

@app.route('/')
def index():
    return render_template('index.html')

# Route to toggle the LED
@app.route('/toggle', methods=['POST'])
def toggle_led():
    global led_on
    data = request.json  # Expecting {"state": 1} or {"state": 0}
    led_on = data['state'] == 1
    GPIO.output(LED_PIN, GPIO.HIGH if led_on else GPIO.LOW)  # Toggle LED
    return jsonify({"status": "success", "led_state": led_on})

app.run(host='0.0.0.0',port=5000)