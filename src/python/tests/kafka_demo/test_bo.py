from kafka_demo.bo import KafkaDemoBO, LocalStorageBO
from kafka_demo.msg import KafkaTestMessage, ProductMessage, ProductSQLMessage, ProductIRISMessage
import random

class TestKafkaDemoBo:
    def test_on_kafka_message(self):
        kafka_demo_bo = KafkaDemoBO()
        kafka_demo_bo.kafka_broker = ['localhost:29092']
        kafka_demo_bo.on_init()
        kafka_message = KafkaTestMessage(name='test', price=1.0)
        kafka_demo_bo.on_kafka_test_message(kafka_message)
        assert True

    def test_run_10_kafka_messages(self):
        kafka_demo_bo = KafkaDemoBO()
        kafka_demo_bo.kafka_broker = ['localhost:29092']
        kafka_demo_bo.on_init()
        for i in range(10):
            import random, string
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(10))
            kafka_message = KafkaTestMessage(name=random_string, price=float(random.random()))
            kafka_demo_bo.on_kafka_test_message(kafka_message)
        assert True

class TestLocalStorageBo:
    def test_on_product_message(self):
        local_storage_bo = LocalStorageBO()
        local_storage_bo.connection_string = 'iris://superuser:SYS@localhost:58809/IRISAPP'
        local_storage_bo.on_init()
        product_message = ProductMessage(name='test', price=1.0)
        local_storage_bo.on_product_message(product_message)
        assert True

    def test_on_product_sql_message(self):
        local_storage_bo = LocalStorageBO()
        local_storage_bo.connection_string = 'iris://superuser:SYS@localhost:58809/IRISAPP'
        local_storage_bo.on_init()
        product_sql_message = ProductSQLMessage(name='test', price=1.0)
        local_storage_bo.on_product_sql_message(product_sql_message)
        assert True

    def test_on_product_iris_message(self):
        local_storage_bo = LocalStorageBO()
        local_storage_bo.on_init()
        product_iris_message = ProductIRISMessage(name='test', price=1.0)
        local_storage_bo.on_product_iris_message(product_iris_message)
        assert True