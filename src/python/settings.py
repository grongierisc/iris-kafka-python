from kafka_demo.bo import KafkaDemoBO, LocalStorageBO
from kafka_demo.bp import KafkaDemoBP
from kafka_demo.bs import KafkaDemoBS, KafkaRestBS

CLASSES = {
    'Python.KafkaDemoBO': KafkaDemoBO,
    'Python.LocalStorageBO': LocalStorageBO,
    'Python.KafkaDemoBP': KafkaDemoBP,
    'Python.KafkaDemoBS': KafkaDemoBS,
    'Python.KafkaRestBS': KafkaRestBS
}

PRODUCTIONS = [
{
    "Python.Production": {
        "@Name": "Python.Production",
        "@TestingEnabled": "true",
        "@LogGeneralTraceEvents": "false",
        "Description": "",
        "ActorPoolSize": "2",
        "Item": [
            {
                "@Name": "Python.KafkaDemoBO",
                "@Category": "",
                "@ClassName": "Python.KafkaDemoBO",
                "@PoolSize": "1",
                "@Enabled": "true",
                "@Foreground": "false",
                "@Comment": "",
                "@LogTraceEvents": "false",
                "@Schedule": ""
            },
            {
                "@Name": "Python.LocalStorageBO",
                "@Category": "",
                "@ClassName": "Python.LocalStorageBO",
                "@PoolSize": "1",
                "@Enabled": "true",
                "@Foreground": "false",
                "@Comment": "",
                "@LogTraceEvents": "false",
                "@Schedule": ""
            },
            {
                "@Name": "Python.KafkaDemoBP",
                "@Category": "",
                "@ClassName": "Python.KafkaDemoBP",
                "@PoolSize": "1",
                "@Enabled": "true",
                "@Foreground": "false",
                "@Comment": "",
                "@LogTraceEvents": "false",
                "@Schedule": ""
            },
            {
                "@Name": "Python.KafkaDemoBS",
                "@Category": "",
                "@ClassName": "Python.KafkaDemoBS",
                "@PoolSize": "1",
                "@Enabled": "true",
                "@Foreground": "false",
                "@Comment": "",
                "@LogTraceEvents": "false",
                "@Schedule": "",
                "Setting": [
                    {
                        "@Target": "Adapter",
                        "@Name": "GroupID",
                        "#text": "demo-group"
                    },
                    {
                        "@Target": "Adapter",
                        "@Name": "Servers",
                        "#text": "kafka:9092"
                    },
                    {
                        "@Target": "Adapter",
                        "@Name": "Topic",
                        "#text": "kafka_demo"
                    }
                ]
            },
            {
                "@Name": "EnsLib.Kafka.Service",
                "@Category": "",
                "@ClassName": "EnsLib.Kafka.Service",
                "@PoolSize": "1",
                "@Enabled": "true",
                "@Foreground": "false",
                "@Comment": "",
                "@LogTraceEvents": "true",
                "@Schedule": "",
                "Setting": [
                    {
                        "@Target": "Host",
                        "@Name": "TargetConfigNames",
                        "#text": "Python.KafkaDemoBP"
                    },
                    {
                        "@Target": "Adapter",
                        "@Name": "GroupID",
                        "#text": "demo-group"
                    },
                    {
                        "@Target": "Adapter",
                        "@Name": "Servers",
                        "#text": "kafka:9092"
                    },
                    {
                        "@Target": "Adapter",
                        "@Name": "Topic",
                        "#text": "kafka_demo"
                    }
                ]
            },
            {
                "@Name": "Python.KafkaRestBS",
                "@Category": "",
                "@ClassName": "Python.KafkaRestBS",
                "@PoolSize": "0",
                "@Enabled": "true",
                "@Foreground": "false",
                "@Comment": "",
                "@LogTraceEvents": "false",
                "@Schedule": ""
            }
        ]
    }
}
]