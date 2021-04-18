import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):


    def connect(self):
        self.accept()
        self.counter = 0
        print("Socket connect")
        print(dir(self.scope))

    def disconnect(self, close_code):
        print("Socket disconnect")
        pass

    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': f"{message} {self.counter}"
        }))

        self.counter += 1