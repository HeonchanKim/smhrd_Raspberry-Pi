from flask import Flask
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)

app = Flask(__name__)
@app.route("/")
def Hello():
    return "hello"

@app.route("/led/on")
def led_on():
    gpio.output(18,gpio.HIGH)
    return "ledon"

@app.route("/led/off")
def led_off():
    gpio.output(18,gpio.LOW)
    return "ledoff"

if __name__ == "__main__":
    app.run()