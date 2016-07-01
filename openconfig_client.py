#!/usr/bin/env python
# Copyright (C) 2016  Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

"""The Python implementation of a gRPC OpenConfig client."""

from __future__ import print_function

import argparse
import sys

from grpc.beta import implementations
import grpc.framework.interfaces.face

import pyopenconfig.pb2
import pyopenconfig.resources

_TIMEOUT_SECONDS = 30


def get(stub, path_str):
    """Get and echo the response"""
    response = stub.Get(pyopenconfig.resources.make_get_request(path_str), _TIMEOUT_SECONDS)
    print(response)


def subscribe(stub, path_str):
    """Subscribe and echo the stream"""
    subscribe_request = pyopenconfig.resources.make_subscribe_request(path_str=path_str)
    i = 0
    try:
        for response in stub.Subscribe([subscribe_request], _TIMEOUT_SECONDS):
            print(response)
            i += 1
    except grpc.framework.interfaces.face.face.AbortionError, error: # pylint: disable=catching-non-exception
        if error.code == grpc.StatusCode.OUT_OF_RANGE and error.details == 'EOF':
            # https://github.com/grpc/grpc/issues/7192
            sys.stderr.write('EOF after %d updates\n' % i)
        else:
            raise


def run():
    """Main loop"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost',
                        help='OpenConfig server host')
    parser.add_argument('--port', type=int, default=6042,
                        help='OpenConfig server port')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--get',
                       help='OpenConfig path to perform a single-shot get')
    group.add_argument('--subscribe',
                       help='OpenConfig path to subscribe to')
    args = parser.parse_args()

    channel = implementations.insecure_channel(args.host, args.port)
    stub = pyopenconfig.pb2.beta_create_OpenConfig_stub(channel)
    if args.get:
        get(stub, args.get)
    elif args.subscribe:
        subscribe(stub, args.subscribe)
    else:
        subscribe(stub, '/')


if __name__ == '__main__':
    run()
