#!/bin/sh
# Copyright (C) 2016  Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

set -e

curl -s https://api.github.com/repos/openconfig/reference/git/refs/heads/master | jq -r .object.sha > reference_version
version=$(cat reference_version)
echo "Downloading openconfig.proto@$version"
curl -s https://api.github.com/repos/openconfig/reference/contents/rpc/openconfig/openconfig.proto?ref=$version -H "Accept: application/vnd.github.VERSION.raw" > openconfig.proto
protoc -I .:$GOPATH/src --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` openconfig.proto
# Fix up the import of any.proto (https://github.com/openconfig/reference/issues/24)
sed -i "" "s/github.com.golang.protobuf.ptypes.any/google.protobuf/" openconfig_pb2.py
sed -i "" "s/github_dot_com_dot_golang_dot_protobuf_dot_ptypes_dot_any_dot_any__pb2/google_dot_protobuf_dot_any__pb2/" openconfig_pb2.py
mv -v openconfig_pb2.py pb2.py
rm openconfig.proto openconfig_pb2.py.bak
