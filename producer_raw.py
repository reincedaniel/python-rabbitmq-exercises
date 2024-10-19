import pika

HOST = "localhost"
PORT = 5672
USERNAME = "guest"
PASSWORD = "guest"
QUEUE_NAME = "data_queue"


connection_parameters = pika.ConnectionParameters(
    host=HOST,
    port=5672,
    credentials=pika.PlainCredentials(username=USERNAME, password=PASSWORD),
)