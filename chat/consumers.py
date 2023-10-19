from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.html import json

class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.group_name = "dj_group"
		if self.channel_layer:
			await self.channel_layer.group_add(
				self.group_name,
				self.channel_name
			)
		await self.accept()

	async def disconnect(self, code):
		if self.channel_layer:
			await self.channel_layer.group_discard(
				self.group_name,
				self.channel_name
			)
		await self.close()

	async def receive(self, text_data):
		print(self.channel_name, self.group_name)
		data = json.loads(text_data)
		username = data["username"]
		message = data["message"]

		if self.channel_layer:
			await self.channel_layer.group_send(
				self.group_name, {
					"type": "sendMessage",
					"username": username,
					"message": message
				}
			)

	async def sendMessage(self, data):
		username = data["username"]
		message = data["message"]

		await self.send(text_data=json.dumps({
			"username": username,
			"message": message
		}))