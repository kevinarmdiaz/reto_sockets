from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from device_backend.devices.models import Device, AlertDevice
from device_backend.devices.api.serializers import AlertDeviceSerializer, DeviceSerializer


class DeviceCreateAPIView(generics.CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class AlertDeviceCreateAPIView(generics.CreateAPIView):
    queryset = AlertDevice.objects.all()
    serializer_class = AlertDeviceSerializer

class DeviceListAPIView(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class AlertDeviceListAPIView(generics.ListAPIView):
    queryset = AlertDevice.objects.all()
    serializer_class = AlertDeviceSerializer

    # def get_queryset(self):
    #     kwarg_slug = self.kwargs.get("slug")
    #     return AlertDevice.objects.filter(question__slug=kwarg_slug).order_by("-created_at")

class DeviceRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class AlertDeviceRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlertDevice.objects.all()
    serializer_class = AlertDeviceSerializer
