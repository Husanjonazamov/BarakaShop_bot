from environs import Env


env =  Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
ADMIN = env('ADMIN')
GROUP_ID = env('GROUP_ID')
WEBAPP_URL = env('WEBAPP_URL')
BASE_URL = env('BASE_URL')

