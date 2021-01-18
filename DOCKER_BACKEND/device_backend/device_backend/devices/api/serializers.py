from rest_framework import serializers
from device_backend.devices.models import Device, AlertDevice


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class AlertDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertDevice
        fields = '__all__'
