from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Device
import websockets
import json
import asyncio

uri = "ws://localhost:8889"

async def send_socket_data(json_data):
    async with websockets.connect(uri) as websocket:
        json_data = json.dumps(json_data)
        await websocket.send(json_data)
        print("Enviando threshold al dispositivo")
        received = await websocket.recv()
        json_received = json.loads(received)
        print(json_received)

@receiver(pre_save, sender=Device)
def send_threshold(sender, instance, *args, **kwargs):
    previous = Device.objects.get(id=instance.id).threshold_temperature
    new_value = instance.threshold_temperature
    if previous!= new_value:
        json_data = {"id":instance.pk, "threshold_temperature":instance.threshold_temperature, "socket_threshold": True}
        try:
            loop = asyncio.new_event_loop()
            loop.run_until_complete(send_socket_data(json_data))
            loop.close()
            print(" Envio de threshold al dispositivo exitoso")
        except Exception as x:
            print("Error al enviar datos al socket.")
        

    
