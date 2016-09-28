#!/bin/sh

# Copyright (C) 2016  Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

if [ "$#" -lt 2 ]
then
   echo "usage: $0 <os> <arch>"
   echo "example: $0 linux i686"
   exit 1
fi

set -e

os=$1
arch=$2
version=$(git describe --tags --match "v[0-9]*" --abbrev=7 HEAD)
cmd="fpm -v $version -n pyopenconfig -s python -t rpm --rpm-os $os -a $arch --epoch 0 setup.py"
echo $cmd
$cmd
