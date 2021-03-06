# Copyright 2008-2018 Univa Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import find_packages, setup


setup(
    name='tortuga-openstack-adapter',
    version='6.3.0',
    url='http://univa.com',
    author='Univa Corp',
    author_email='info@univa.com',
    license='Commercial',
    packages=find_packages(exclude=['tortuga_kits']),
    namespace_packages=[
        'tortuga',
        'tortuga.resourceAdapter'
    ],
    zip_safe=False,
    install_requires=[
        'requests',
        'gevent',
    ]
)
