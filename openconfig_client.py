#!/usr/bin/env python
# Copyright (C) 2016  Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

"""The Python implementation of a gRPC OpenConfig client."""

from __future__ import print_function

import argparse
import sys

import grpc
import grpc.framework.interfaces.face

import pyopenconfig.openconfig_pb2
import pyopenconfig.resources


def get(stub, path_str, metadata):
    """Get and echo the response"""
    response = stub.Get(pyopenconfig.resources.make_get_request(path_str),
                        metadata=metadata)
    print(response)


def subscribe(stub, path_str, metadata):
    """Subscribe and echo the stream"""
    subscribe_request = pyopenconfig.resources.make_subscribe_request(path_str=path_str)
    i = 0
    try:
        for response in stub.Subscribe(subscribe_request, metadata=metadata):
            print(response)
            i += 1
    except grpc.framework.interfaces.face.face.AbortionError, error:  # pylint: disable=catching-non-exception
        if error.code == grpc.StatusCode.OUT_OF_RANGE and error.details == 'EOF':
            # https://github.com/grpc/grpc/issues/7192
            sys.stderr.write('EOF after %d updates\n' % i)
        else:
            raise


def run():
    """Main loop"""
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--host', default='localhost',
                        help='OpenConfig server host')
    parser.add_argument('--port', type=int, default=6042,
                        help='OpenConfig server port')
    parser.add_argument('--username', type=str, help='username')
    parser.add_argument('--password', type=str, help='password')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--get',
                       help='OpenConfig path to perform a single-shot get')
    group.add_argument('--subscribe', default='/',
                       help='OpenConfig path to subscribe to')
    args = parser.parse_args()

    metadata = None
    if args.username or args.password:
        metadata = [("username", args.username), ("password", args.password)]

    channel = grpc.insecure_channel(args.host + ":" + str(args.port))
    stub = pyopenconfig.openconfig_pb2.OpenConfigStub(channel)
    if args.get:
        get(stub, args.get, metadata)
    else:
        subscribe(stub, args.subscribe, metadata)


if __name__ == '__main__':
    run()
