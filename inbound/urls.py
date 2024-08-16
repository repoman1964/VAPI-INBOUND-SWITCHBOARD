from django.urls import path



from .views import (
    testAndDirectInboundCall,   
    )

app_name = 'inbound'  # Declaring the namespace for this URLs module

urlpatterns = [

    path('controller/', testAndDirectInboundCall, name='inbound_controller'),
]

