from flask import Flask, request, jsonify

import intersystems_iris

import json

# Create a connection to InterSystems IRIS
conn = intersystems_iris.connect("localhost", 55223, "IRISAPP", "SuperUser", "SYS")

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
        bs.invoke("OnProcessInput",message)
        
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    return jsonify({"message": "Message sent to KafkaDemoBP"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)