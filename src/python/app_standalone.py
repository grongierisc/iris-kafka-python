from flask import Flask, request, jsonify

import intersystems_iris

import json

import os
# Create a connection to InterSystems IRIS
conn = intersystems_iris.connect(
    hostname=os.getenv('IRIS_HOST', 'iris'),
    port=int(os.getenv('IRIS_PORT', 1972)),
    namespace=os.getenv('IRIS_NAMESPACE', 'IRISAPP'),
    username=os.getenv('IRIS_USERNAME', 'SuperUser'),
    password=os.getenv('IRIS_PASSWORD', 'SYS')
)

app = Flask(__name__)

@app.route('/kafka', methods=['POST'])
def kafka_demo():
    message = json.dumps(request.get_json())

    #### Equivalent to Director.create_python_business_service('Python.KafkaRestBS')
    irisInstance = intersystems_iris.IRIS(conn)
    bs = irisInstance.classMethodObject("EnsLib.PEX.Director","dispatchCreateBusinessService","Python.KafkaRestBS")
    #### End of equivalent

    try:

        #### Equivalent to bs.on_process_input(message)
        status = bs.invoke("OnProcessInput",message)
        if status != 1:
            raise Exception("Error processing the message")

    except Exception as e:
        return jsonify({"message": str(e)}), 500
    return jsonify({"message": "Message sent to KafkaDemoBP"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)