from tornado import websocket, web, ioloop, options
from tornado.web import url
import logging
import json
import signal 
import asyncio
from random import randint
import websockets
from datetime import datetime, timedelta
import pytz
import requests

code_device  = "1"
tz_ = pytz.timezone('America/Bogota') 
HOST = "127.0.0.1"
PORT_DJANGO = 8000
PORT_SERVER = 8889
ENDPOINT = f'http://{HOST}:{PORT_DJANGO}'
ENDPOINT_CREATE_ALERTS = f'{ENDPOINT}/api/alerts/create/'



class DeviceSocket(websocket.WebSocketHandler):
    device_threshold = []
    new_threshold = True
    def check_origin(self, origin):
        return True

    def open(self):
        logging.info("A client connected.")

    def on_close(self):
        logging.info("A client disconnected")

    def on_message(self, message):
        try: 
            json_received = json.loads(message)
            
            if  self.new_threshold and not "socket_threshold" in json_received:
                logging.info("Obteniendo limite de temperatura")
                self.device_threshold.append({
                                             "id": json_received["id"],
                                             "threshold_temperature": self.get_threshold(json_received["id"]),
                                            })
                self.new_threshold = False
            if not "socket_threshold" in json_received:
                json_received = self.set_threshold(json_received)
            json_received = self.check_json(json_received)
            self.write_message(json.dumps(json_received))
            
        except Exception as x:
            logging.info(x)
    

    def set_threshold(self, json_to_change):
        for change in self.device_threshold:
            if change["id"] == json_to_change["id"]:
                json_to_change["threshold_temperature"] = change["threshold_temperature"]
        return json_to_change
        



    def create_alerts(self, json_data):
        response = requests.post(ENDPOINT_CREATE_ALERTS, data = json_data)
        logging.info(f'La alerta para device {json_data["device"]} ha sido creada: ')

    def update_data_device(self, json_data):
        #Actualizar valor de last_temperature o keep_alive
        response = requests.patch(f"{ENDPOINT}/api/devices/{json_data['id']}/", data = json_data)
        logging.info(f'DEVICE {json_data["id"]} actualizado: ')

    def get_threshold(self, device_id):
        response = requests.get(f"{ENDPOINT}/api/devices/{device_id}/")
        return response.json()['threshold_temperature']

    def check_json(self, json_received):
        if "temperature" in json_received:
            data = {
            "id": json_received["id"],
            "last_temperature": json_received["temperature"],
            }
            self.update_data_device(data)
            if json_received["temperature"] > json_received["threshold_temperature"]: 
                data = {"device":json_received["id"], 
                        "description":f"""La temperatura: {json_received['temperature']} 
                                        ha superado el valor de {json_received['threshold_temperature']}""",
                        "temperature": json_received["temperature"],
                        }
                self.create_alerts(data)
        elif "timestamp" in json_received:
            data = {
                "id": json_received["id"],
                "keep_alive": json_received["timestamp"]
            }
            print(data)
            self.update_data_device(data)
        
        elif "socket_threshold" in json_received:
            print(json_received)
            for device in self.device_threshold:
                if device["id"] == json_received["id"]:
                    device["threshold_temperature"] = json_received["threshold_temperature"]
            print(self.device_threshold)
            

        return json_received

        
def start_app(*args, **kwargs):
    application = Server([
            (r'/', DeviceSocket),
    ])
    application.listen(PORT_SERVER)
    print(f"Starting Server... {code_device}")
    return application


class Server(web.Application):
    is_closing = False

    def signal_handler(self, signum, frame):
        print("Turning off the device... ")
        self.is_closing = True
    
    def try_exit(self):
        if self.is_closing:
            ioloop.IOLoop.instance().stop()
            print(" Shutdown complete. ")

            

if __name__ == '__main__':
    server = start_app()
    options.parse_command_line()
    signal.signal(signal.SIGINT, server.signal_handler)
    ioloop.PeriodicCallback(server.try_exit, 100).start()
    ioloop.IOLoop.instance().start()