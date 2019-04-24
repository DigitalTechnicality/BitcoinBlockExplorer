import websocket
import asyncio
import json
import json
import ssl
import asyncio

async def Connection():
    ws = websocket.create_connection('wss://ws.blockchain.info/inv')
    if (ws.connect('wss://ws.blockchain.info/inv')):
            print("connected")
    ws.send('{"op":"unconfirmed_sub"}')
    while True:
        indata = (ws.recv())
        j = json.loads(indata)
    #print(j)
    #print(j["x"])
        print(j["x"]["inputs"])
