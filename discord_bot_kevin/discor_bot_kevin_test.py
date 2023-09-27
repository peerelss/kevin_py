import discord
from discord.ext import commands

client = discord.Client()


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')


@client.event
async def on_message(message):
    print(message)
    if message.attachments:
        for attachment in message.attachments:
            # 下载附件
            await attachment.save(f"received_files/{attachment.filename}")
            # 发送回复消息以确认文件已接收
            await message.channel.send(f"文件 '{attachment.filename}' 已接收！")
    if message.content == 'hello':
        await message.channel.send('Hello!')


# Replace YOUR_BOT_TOKEN with your bot token
client.run('MTEwMzQ5MjMzMTQzNDQxNDEwMQ.G05mF9.XLECddf6qXw0uP3Hh0XQ2j091Vwy2FEKTt6s1E')
