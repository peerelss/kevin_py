import websocket


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print("### connected ###")

    # 发送消息
    ws.send("Hello, Server!")


if __name__ == "__main__":
    # 连接 WebSocket 服务器
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://172.16.12.80:5050/echo ",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    # 启动 WebSocket
    ws.run_forever()
