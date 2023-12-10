# Installing paho-mqtt - [For further documentation](https://pypi.org/project/paho-mqtt/#usage-and-api)
## The latest stable version is available in the Python Package Index (PyPi) and can be installed using
```
pip install paho-mqtt
```
## Or with virtualenv:
```
virtualenv paho-mqtt
source paho-mqtt/bin/activate
pip install paho-mqtt
```
## To obtain the full code, including examples and tests, you can clone the git repository:
```
git clone https://github.com/eclipse/paho.mqtt.python
```
## Once you have the code, it can be installed from your repository as well:
```
cd paho.mqtt.python
python setup.py install
```
## To perform all test (including MQTT v5 test), you also need to clone paho.mqtt.testing in paho.mqtt.python folder:
```
git clone https://github.com/eclipse/paho.mqtt.testing.git
```