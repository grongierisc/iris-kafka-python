#!/bin/bash

set -m

fg %1

/usr/irissys/dev/Cloud/ICM/waitISC.sh

# init iop
iop --init

# load production
iop -m /irisdev/app/src/python/settings.py

# start the flask app
cd /irisdev/app/src/python
python3 app.py &

# start production
iop --start Python.Production
