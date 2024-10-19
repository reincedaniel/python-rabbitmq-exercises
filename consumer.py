import pika


HOST = "localhost"
PORT = 5672
USERNAME = "guest"
PASSWORD = "guest"
QUEUE_NAME = "data_queue"


class RabbitmqConsumer:
    def __init__(self, callback):
        self.__host = HOST
        self.__port = PORT
        self.__username = USERNAME
        self.__password = PASSWORD
        self.__queue = QUEUE_NAME
        self.__callback = callback
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(username=self.__username, password=self.__password),
        )

        channel = pika.BlockingConnection(connection_parameters).channel()
        channel.queue_declare(queue=self.__queue, durable=True)
        channel.basic_consume(
            queue=QUEUE_NAME, auto_ack=True, on_message_callback=self.__callback
        )
        
        return channel

    def start(self):
        print(f"Listening RabbitMQ :::: #consumer on PORT {PORT}")
        self.__channel.start_consuming()
    

# ----------------------------------------

def message_callback(chan, method, properties, body):
        print(body)

rabbitmq_consumr = RabbitmqConsumer(message_callback)
rabbitmq_consumr.start()