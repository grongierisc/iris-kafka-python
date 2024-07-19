import sys
from os.path import dirname as d
from os.path import abspath,join
root_dir = d(d(abspath(__file__)))
# add root to path
sys.path.append(root_dir)
sys.path.append(join(root_dir,"kafka_demo"))

