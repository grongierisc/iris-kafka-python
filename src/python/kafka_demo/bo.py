from iop import BusinessOperation
from kafka import KafkaProducer
from kafka_demo.msg import KafkaMessage

class KafkaDemoBO(BusinessOperation):
    # simple business operation to process a message to a Kafka topic
    def on_init(self):
        if not hasattr(self, 'topic'):
            # default topic
            self.topic = 'kafka_demo'
        if not hasattr(self, 'kafka_broker'):
            # default Kafka broker
            self.kafka_broker = 'localhost:9092'
        # initialize the Kafka producer
        self.producer = KafkaProducer(bootstrap_servers=self.kafka_broker)

    def on_kafka_message(self, msg: KafkaMessage):
        # send the message to the Kafka topic
        self.producer.send(self.topic, msg.message.encode())
        self.producer.flush()

    def on_tear_down(self):
        # close the Kafka producer
        self.producer.close()
