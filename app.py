from crypt import methods
from flask import Flask, render_template, request
import serial

app = Flask(__name__)

try:
    arduino = serial.Serial("/dev/ttyACM0", 9600)
    print("Arduino conectado")
except:
    print("Arduino no conectado") 

@app.route("/", methods=["GET", "POST"])
def index():
    
    return render_template("index.html")

@app.route("/control/temperature", methods=["GET", "POST"])
def control_temperature():
    if request.method == "POST":
        iotDevice = request.form["iot-device"]
        if iotDevice == "Turn on lamp":
            arduino.write(b"1")
        elif iotDevice == "Turn off lamp":
            arduino.write(b"2")

    return render_template("temperature.html")

@app.route("/control/security", methods=["POST", "GET"])
def control_security():

    return render_template("security.html")

@app.route("/control/food", methods=["POST", "GET"])
def control_food():

    return render_template("food.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
