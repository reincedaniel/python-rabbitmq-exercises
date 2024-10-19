import pika

HOST = "localhost"
PORT = 5672
USER_NAME = "guest"
PASSWORD = "guest"
QUEUE_NAME = "data_queue"


def message_callback(chan, method, properties, body):
    print(body)

connection_parameters = pika.ConnectionParameters(
    host=HOST,
    port=5672,
    credentials=pika.PlainCredentials(username=USER_NAME, password=PASSWORD),
)

channel = pika.BlockingConnection(connection_parameters).channel()
channel.queue_declare(queue=QUEUE_NAME, durable=True)
channel.basic_consume(queue=QUEUE_NAME, auto_ack=True, on_message_callback=message_callback)

print(f"Listening RabbitMQ:::: #consumer! on PORT {PORT}")
channel.start_consuming()