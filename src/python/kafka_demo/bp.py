from iop import BusinessProcess
from kafka_demo.msg import KafkaRawMessage, ProductMessage, ProductSQLMessage, ProductIRISMessage, Product

import random
import json

class KafkaDemoBP(BusinessProcess):
    def on_kafka_raw_message(self, msg: KafkaRawMessage):
        # deserialize the message to a Product
        deserialized_msg = json.loads(msg.value.decode('utf-8'))
        # parse the message to a Product
        product = Product(**deserialized_msg)
        # randomely choose the message type
        message_type = random.choice([ProductMessage, ProductSQLMessage, ProductIRISMessage])
        # send the message to the business operation
        self.send_request_sync('Python.LocalStorageBO', message_type(**product.__dict__))

    def on_iris_kafka_message(self, msg: 'iris.EnsLib.Kafka.Message'):
        # transform the iris message to a KafkaRawMessage
        kafka_message = KafkaRawMessage(msg.value.encode('utf-8'))
        # pass it to the main business process
        self.on_kafka_raw_message(kafka_message)

        