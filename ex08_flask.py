from flask import Flask
import led18
import ex07_select as s

app = Flask(__name__)
@app.route("/")
def Hello():
    return "<h1>Hello World</h1>"

@app.route("/led/on")
def led_on():
    led18.ledon()
    return "ledon"

@app.route("/led/off")
def led_off():
    led18.ledoff()
    return "ledoff"

@app.route("/select")
def select():
    r = s.select_sensordb()
    return r

if __name__ == "__main__":
    app.run()
    #host="172.30.1.53"

