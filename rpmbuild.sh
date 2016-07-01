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
cmd="fpm -s python -t rpm --rpm-os $os -a $arch --epoch 0 setup.py"
echo $cmd
$cmd
