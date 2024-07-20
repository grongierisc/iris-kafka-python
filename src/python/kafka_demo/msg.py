from iop import Message
from dataclasses import dataclass

@dataclass
class Product:
    name: str = ""
    price: float = 0.0

@dataclass
class KafkaTestMessage(Message, Product):
    pass

@dataclass
class ProductMessage(Message, Product):
    pass

@dataclass
class ProductSQLMessage(Message, Product):
    pass

@dataclass
class ProductIRISMessage(Message, Product):
    pass

@dataclass
class KafkaRawMessage(Message):
    value: bytes = b''

