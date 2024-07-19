from kafka_demo.bo import KafkaDemoBO
from kafka_demo.msg import KafkaMessage

class TestKafkaDemoBo:
    def test_on_kafka_message(self):
        kafka_demo_bo = KafkaDemoBO()
        kafka_demo_bo.on_init()
        kafka_message = KafkaMessage('message')
        kafka_demo_bo.on_kafka_message(kafka_message)
        assert True