import os

DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
HOST_ADDRESS = os.environ['HOST_ADDRESS']
DB_NAME = os.environ['DB_NAME']
# ENV = os.environ['ENV']
DATABASE = os.environ['DATABASE']
RABBITMQ_BROKER = os.getenv('RABBITMQ_BROKER', 'amqp://guest:guest@localhost:5672/')
