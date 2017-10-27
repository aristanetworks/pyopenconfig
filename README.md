[![Build Status](https://travis-ci.org/aristanetworks/pyopenconfig.svg?branch=master)](https://travis-ci.org/aristanetworks/pyopenconfig)

# pyopenconfig

Python client and library for the [OpenConfig](http://openconfig.net) gRPC interface.

The version of the gRPC proto definition being uses is tracked in [pyopenconfig/reference_version](pyopenconfig/reference_version).

# DEPRECATED

Please refer to [gnmi/proto](https://github.com/openconfig/gnmi/tree/master/proto/gnmi) for the generated Python code to access the gNMI service.

If you're looking for a command-line tool to access gNMI check out [gnmi](https://github.com/aristanetworks/goarista/tree/master/cmd/gnmi).

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
  --username USERNAME   username
  --password PASSWORD   password
  --get GET             OpenConfig path to perform a single-shot get (default:
                        None)
  --subscribe SUBSCRIBE
                        OpenConfig path to subscribe to (default: /)
```

#### Sample usage

```
openconfig_client.py --host arista --port 6042 --get /vlans/vlan/42
```
