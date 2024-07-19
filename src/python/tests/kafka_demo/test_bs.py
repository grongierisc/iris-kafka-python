from kafka_demo.bs import KafkaDemoBS
from kafka_demo.msg import KafkaMessage
from unittest.mock import MagicMock

class TestKafkaDemoBs:
    def test_on_process_input(self):
        kafka_demo_bs = KafkaDemoBS()
        kafka_demo_bs.on_init()
        # mock send_request_async
        kafka_demo_bs.send_request_async = MagicMock()
        kafka_demo_bs.on_process_input('')
        assert True