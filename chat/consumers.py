from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		await self.accept()

	async def disconnect(self, code):
		await self.close()

	async def receive(self, text_data=None):
		print(text_data)
		await self.send(text_data)