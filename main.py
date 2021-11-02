""" initial state """
from config.parameters import HTTP_PORT, LOCAL_HOST
from uvicorn import Server, Config

server = Server(Config("service.server:app", host=LOCAL_HOST, port=HTTP_PORT))

if __name__ == '__main__':
    server.run()
