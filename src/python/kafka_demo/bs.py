from iop import BusinessService
from kafka import KafkaConsumer
from kafka_demo.msg import KafkaMessage
import iris

class KafkaDemoBS(BusinessService):
    @staticmethod
    def get_adapter_type():
        return "Ens.InboundAdapter"
    
    def on_init(self):
        if not hasattr(self, 'topic'):
            # default topic
            self.topic = 'kafka_demo'
        if not hasattr(self, 'kafka_broker'):
            # default Kafka broker
            self.kafka_broker = 'localhost:9092'
        if not hasattr(self, 'timeout'):
            # default timeout
            self.timeout = '5'
        # initialize the Kafka consumer
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.kafka_broker,
            group_id='demo-group',
            auto_offset_reset='smallest',
            enable_auto_commit=True,
            consumer_timeout_ms=int(self.timeout) * 1000
        )
        # get the offset
        self.offset = iris.gref("^KafkaDemo.Offset")

    def on_tear_down(self):
        # close the Kafka consumer
        self.consumer.close()

    def on_process_input(self, message_input):
        # consume messages from the Kafka topic
        for msg in self.consumer:
            # store the offset
            self.offset[self.topic] = msg.offset
            # create a Kafka message
            kafka_message = KafkaMessage(msg.value.decode())
            # send the Kafka message to the business process
            self.send_request_async('target', kafka_message)
            # break the loop
            break
        