#!/bin/sh
# Copyright (C) 2016  Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

protoc  --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` openconfig.proto
