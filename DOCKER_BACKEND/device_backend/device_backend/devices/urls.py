from django.urls import path

import device_backend.devices.api.views as views


app_name = "devices"
urlpatterns = [
    path("devices/create/", view=views.DeviceCreateAPIView.as_view(), name="device-create"),
    path('devices/', views.DeviceListAPIView.as_view(), name='device-list'),
    path('alerts/', views.AlertDeviceListAPIView.as_view(), name='alertdevice-list'),
    path('alerts/create/', views.AlertDeviceCreateAPIView.as_view(), name='alertdevice-list'),
    path("alerts/<int:pk>/", 
         views.AlertDeviceRUDAPIView.as_view(),
         name="alert-detail"),
    path("devices/<int:pk>/", 
         views.DeviceRUDAPIView.as_view(),
         name="device-detail"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
