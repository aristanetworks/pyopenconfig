# pyopenconfig

Python client and library for the [OpenConfig](http://openconfig.net) gRPC interface.

## Installation

```
pip install git+git://github.com/aristanetworks/pyopenconfig.git
```

### Usage
```
usage: openconfig_client.py [-h] [--host HOST] [--port PORT]
                            [--get GET | --subscribe SUBSCRIBE]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           OpenConfig server host
  --port PORT           OpenConfig server port
  --get GET             OpenConfig path to perform a single-shot get
  --subscribe SUBSCRIBE
                        OpenConfig path to subscribe to
```

#### Sample usage

```
openconfig_client.py --host arista --port 6042 --get /vlans/vlan/42
```
