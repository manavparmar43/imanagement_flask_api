from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool("FLASK_DEBUG", default=False)