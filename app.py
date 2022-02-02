from flask import Flask, render_template, request
import serial

app = Flask(__name__)

try:
    arduino = serial.Serial("/dev/ttyACM1", 9600)
    print("Arduino conectado")
except:
    print("Arduino no conectado") 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        iotDevice = request.form["iot-device"]
        if iotDevice == "Turn on lamp":
            arduino.write(b"1")
        elif iotDevice == "Turn off lamp":
            arduino.write(b"2")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
