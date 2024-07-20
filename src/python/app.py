from flask import Flask, request, jsonify
from kafka_demo.msg import KafkaRawMessage
from iop import Director

import json

app = Flask(__name__)

@app.route('/kafka', methods=['POST'])
def kafka_demo():
    message = request.get_json()
    kafka_raw_message = KafkaRawMessage(json.dumps(message).encode('utf-8'))
    bs = Director.create_python_business_service('Python.KafkaRestBS')
    try:
        bs.on_process_input(kafka_raw_message)
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    return jsonify({"message": "Message sent to KafkaDemoBP"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)