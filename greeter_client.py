import logging
import asyncio
import grpc

from fastapi import FastAPI
from fastapi import APIRouter

import helloworld_pb2
import helloworld_pb2_grpc




server_name = os.getenv("SERVER_NAME", "greet_java")

async def send_message(name) -> None:
	print(f'with server name:{server_name}')
    async with grpc.aio.insecure_channel(f'{server_name}:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = await stub.SayHello(helloworld_pb2.HelloRequest(name=name))
    print("Greeter client received: " + response.message)


RPEFIX = "/hello"

app = FastAPI(openapi_url=f"{PREFIX}/openapi.json", docs_url=f"{PREFIX}/docs")

router = APIRouter()



@router.get("/send")
def send(msg: str):
    print(f'to send message:{msg}')
    asyncio.run(send_message(msg))
    return {"success": True}


app.include_router(
    router,
    prefix=PREFIX
)



