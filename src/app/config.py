import os

RABBITMQ_BROKER = os.getenv('RABBITMQ_BROKER', 'amqp://guest:guest@rabbitmq:5672/')
RABBITMQ_BACKEND = os.getenv('RABBITMQ_BACKEND', 'rpc://')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
HOST_ADDRESS = os.getenv('HOST_ADDRESS', '172.17.0.1:5432')
DB_NAME = os.getenv('DB_NAME', 'test_table')
DATABASE = os.getenv('DATABASE', 'postgres')

