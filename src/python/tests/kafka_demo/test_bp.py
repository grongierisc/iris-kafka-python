from kafka_demo.bp import KafkaDemoBP
from kafka_demo.msg import KafkaRawMessage

from unittest.mock import MagicMock

class TestKafkaDemoBp:
    def test_on_kafka_raw_message(self):
        kafka_demo_bp = KafkaDemoBP()
        kafka_demo_bp.send_request_sync = MagicMock()
        kafka_demo_bp.on_kafka_raw_message(KafkaRawMessage(b'{"name": "test", "price": 1.0}'))
        assert True
