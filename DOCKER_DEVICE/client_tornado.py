from tornado.ioloop import IOLoop, PeriodicCallback
from tornado import options
from tornado.websocket import websocket_connect, WebSocketClosedError
import asyncio
from datetime import datetime, timedelta
import pytz
from random import randint
import signal 

tz_ = pytz.timezone('America/Bogota') 
import json
def generate_random_temp():
    return randint(10, 100)

def get_actual_time():
    return datetime.now(tz_).strftime("%Y-%m-%dT%H:%M:%S")

class Device(object):
    def __init__(self, url, code_device, timeout, threshold=0):
        self.url = url
        self.timeout = timeout
        self.code_device = code_device
        self.ioloop = IOLoop.instance()
        self.is_closing = False
        self.ws = None
        io_loop = IOLoop.current()
        io_loop.spawn_callback(self.connect)
        PeriodicCallback(self.try_exit, 100).start()
        PeriodicCallback(self.keep_alive, 5000).start()
        PeriodicCallback(self.temperature, 10000).start()
        self.ioloop.start()
        options.parse_command_line()
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, signum, frame):
        self.is_closing = True
    
    def try_exit(self):
        if self.is_closing:
            ioloop.IOLoop.instance().stop()
            print(" Shutdown complete. ")

    async def connect(self):
        print( "trying to connect")
        try:
            self.ws = await websocket_connect(self.url)
        except Exception as ex:
            print( "connection error")
        else:
            print( "connected")
            self.run()

    def run(self):
        while True:
            msg = yield self.ws.read_message()
            if msg is None:
                print( "connection closed")
                self.ws = None
                break

    async def keep_alive(self):
        if self.ws is None:
            await self.connect()
        else:
            self.ws.write_message(self.get_json_keep())
            response = json.loads(await self.ws.read_message())
            print(response["threshold_temperature"])

    async def temperature(self):
        if self.ws is None:
            await self.connect()
        else:
            self.ws.write_message(self.get_json_temperature())
            response = json.loads(await self.ws.read_message())
            print(response["threshold_temperature"])

    def get_json_keep(self):
        """Funcion asincronica para enviar keep_alive a traves de sockets"""
        return json.dumps({"id": self.code_device, "timestamp": get_actual_time()})
    
    def get_json_temperature(self):
        """Funcion asincronica para enviar temperatura a traves de sockets"""
        return json.dumps({"id": self.code_device, "temperature": generate_random_temp()})


if __name__ == "__main__":
    code_device  = 1
    try:
        device_ = Device("ws://localhost:8889", code_device, 5)
    except KeyboardInterrupt as x:
        print("Turning off the device... ", code_device)
