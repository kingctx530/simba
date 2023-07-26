
class RoutingUpdateSource:
    def __init__(self):
        self.example_data = """        
#example
#from CPKApp import consumers as cpkapp_consumers
#websocket_urlpatterns = [
    # path("ws/cpk/<str:room_name>/$", cpkapp_consumers.Consumer.as_asgi()),
    #re_path(r"ws/cpk/(?P<room_name>[a-zA-Z0-9\-]+)/$", cpkapp_consumers.Consumer.as_asgi()),
    # re_path(r"ws/chat/(?P<room_name>\w+)/$", mainapp_consumers.MyConsumer.as_asgi())    
#]
from django.urls import re_path, path

websocket_urlpatterns = [
    
]
"""