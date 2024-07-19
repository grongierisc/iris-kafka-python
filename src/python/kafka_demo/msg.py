from iop import Message
from dataclasses import dataclass

@dataclass
class KafkaMessage(Message):
    # simple message class to hold a message to be sent to a Kafka topic
    message: str