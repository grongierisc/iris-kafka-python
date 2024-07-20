from iop import BusinessOperation
from kafka import KafkaProducer
from kafka_demo.models import ProductModel
from kafka_demo.msg import (
    KafkaTestMessage, ProductMessage, ProductSQLMessage,
    ProductIRISMessage
)

import json

import iris

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


class LocalStorageBO(BusinessOperation):
    def on_init(self):
        if not hasattr(self, 'connection_string'):
            # default engine
            self.connection_string = 'iris+emb://'
        self.engine = create_engine(self.connection_string)
        # bind the engine to the ProductModel
        ProductModel.metadata.create_all(self.engine)

    def on_product_message(self, msg: ProductMessage):
        product = ProductModel(name=msg.name, price=msg.price)
        with Session(self.engine) as session:
            session.add(product)
            session.commit()

    def on_product_sql_message(self, msg: ProductSQLMessage):
        with self.engine.connect() as conn:
            # Create your SQL statement with named parameters
            statement = text("INSERT INTO product (name, price) VALUES (:name, :price)")
            
            # Execute the statement with parameters
            conn.execute(statement, {"name": msg.name, "price": msg.price})
            conn.commit()


    def on_product_iris_message(self, msg: ProductIRISMessage):
        product = iris.cls('User.product')._New()
        product.name = msg.name
        product.price = msg.price
        product._Save()


class KafkaDemoBO(BusinessOperation):
    # simple business operation to process a message to a Kafka topic
    def on_init(self):
        if not hasattr(self, 'topic'):
            # default topic
            self.topic = 'kafka_demo'
        if not hasattr(self, 'kafka_broker'):
            # default Kafka broker
            self.kafka_broker = ['kafka:9092']
        # initialize the Kafka producer
        self.producer = KafkaProducer(bootstrap_servers=self.kafka_broker)

    def on_kafka_test_message(self, msg: KafkaTestMessage):
        # create a json from msg
        message = json.dumps(msg.__dict__).encode('utf-8')
        # send the message to the Kafka topic
        self.producer.send(self.topic, message)
        self.producer.flush()

    def on_tear_down(self):
        # close the Kafka producer
        self.producer.close()
