from environs import Env

env = Env()
env.read_env()

""" COMMON ENVIRONS """

HTTP_PORT = env.int("HTTP_PORT", 8000)
LOCAL_HOST = env.str("LOCAL_HOST", "0.0.0.0")
