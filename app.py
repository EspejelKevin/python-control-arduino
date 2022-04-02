from flask import Flask, render_template, request
from connection import Connection
from api import Api

app = Flask(__name__)
app.config["SECRET_KEY"]="development"


@app.route("/", methods=["GET"])
def index():
    
    return render_template("index.html")


@app.route("/control/temperature", methods=["GET"])
def control_temperature():
    try:
        while True:
            datos = conn.read_data()
            api = Api()
            api.post_sensor_temp(int(float(datos[0])))
            api.post_sensor_foto(datos[1])

            return render_template("temperature.html", temperature=datos[0], intensity=int(datos[1]))
    except:
        return """<h1 style='text-align:center; color:red; margin-top: 3rem'>Error connection</h1>
                  <h2 style='text-align:center; color:blue; margin-top: 3rem;'>Try again later</h2>
                  <center style='margin-top:3rem;'><a href='/' style="text-decoration:none; background-color:green; padding:10px; font-size:1rem; color:white; border-radius:5px;">Home</a></center>
               """


@app.route("/control/security", methods=["POST", "GET"])
def control_security():

    """
    
    RECIBIR LOS DATOS DEL ARDUINO PARA MOSTRAR UN MENSAJE DE
    ALERTA
    
    """
    try:
        while True:
            datos = conn.read_data()
            ir = int(datos[2])
            pir = int(datos[3])
            
            
            return render_template("security.html", ir=ir, pir=pir)
    except:
        return """<h1 style='text-align:center; color:red; margin-top: 3rem'>Error connection</h1>
                  <h2 style='text-align:center; color:blue; margin-top: 3rem;'>Try again later</h2>
                  <center style='margin-top:3rem;'><a href='/' style="text-decoration:none; background-color:green; padding:10px; font-size:1rem; color:white; border-radius:5px;">Home</a></center>
               """


@app.route("/control/food", methods=["POST", "GET"])
def control_food():

    """
    
    ENVIAR UN 1 PARA ACTIVAR EL SISTEMA DE COMIDA
    
    """
    if request.method == "POST":
        day = request.form.get("days")
        morning = request.form.get("morning")
        afternoon = request.form.get("afternoon")
        night = request.form.get("night")
        amount = request.form.get("amount")

        api = Api()
        api.post_dispensador(day, amount, morning, afternoon, night)

        conn.send_data()

    
    return render_template("food.html")


if __name__ == "__main__":
    conn = Connection()
    app.run(debug=True, host="0.0.0.0", port=5000)
