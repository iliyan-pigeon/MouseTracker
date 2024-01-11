import json
from channels.generic.websocket import AsyncWebsocketConsumer


class MouseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        x = data['x']
        y = data['y']

        await self.send(text_data=json.dumps({
            'x': x,
            'y': y
        }))