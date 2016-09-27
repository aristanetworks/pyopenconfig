#!/usr/bin/env python
# Copyright (C) 2016  Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

"""Install scripts for pyopenconfig"""

from setuptools import setup, find_packages


setup(
    name="pyopenconfig",
    version="0.0.2",
    packages=find_packages(),
    scripts=['openconfig_client.py'],

    install_requires=['grpcio>=0.15.0'],

    # metadata for upload to PyPI
    author="Giuseppe Valente",
    author_email="gvalente@arista.com",
    description="gRPC OpenConfig client",
    license="ASL",
    keywords="grpc openconfig",
)
