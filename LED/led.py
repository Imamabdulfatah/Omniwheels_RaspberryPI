import RPi.GPIO as GPIO
from flask import Flask, render_template
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
#pin GPIO 3, sebagai output // BCM
#pin nomor 3, sebagai output //BOARD
@app.route('/')
def index():
    return render_template('kontrol_led.html')

@app.route('/on')
def on():
    GPIO.output(3, GPIO.HIGH)
    return render_template('kontrol_led.html')
@app.route('/off')
def off():
    GPIO.output(3, GPIO.LOW)
    return render_template('kontrol_led.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')