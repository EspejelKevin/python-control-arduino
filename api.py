import requests


class Api:
    def post_dispensador(self, day, amount, morning, afternoon, night):
        url = "https://api-iot-v1.herokuapp.com/api/post/dispensador"
 
        payload = {
            "dia":day,
            "hora":"",
            "año": "2022",
            "cantidad": amount
        }

        if morning:
            payload["hora"] = morning
        elif afternoon:
            payload["hora"] = afternoon
        else:
            payload["hora"] = night

        headers = {}
 
        response = requests.request("POST", url, headers=headers, data=payload)

        return response

    def post_sensor_temp(self, temp):
        url = "https://api-iot-v1.herokuapp.com/api/post/sensor"
 
        payload = {
            "tipo":"DHT11",
            "valor":temp
        }

        

        headers = {}
 
        requests.request("POST", url, headers=headers, data=payload)


    def post_sensor_foto(self, intensity):
        url = "https://api-iot-v1.herokuapp.com/api/post/sensor"
 
        payload = {
            "tipo":"Fotoresistencia",
            "valor":intensity
        }

        

        headers = {}
 
        requests.request("POST", url, headers=headers, data=payload)

   
        
