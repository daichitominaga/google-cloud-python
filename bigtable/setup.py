# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os

import setuptools


# Package metadata.

name = 'google-cloud-bigtable'
description = 'Google Cloud Bigtable API client library'
version = '0.28.2.dev1'
# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Stable'
release_status = 'Development Status :: 3 - Alpha'
dependencies = [
    'google-cloud-core<0.29dev,>=0.28.0',
    'google-api-core[grpc]<0.2.0dev,>=0.1.1',
]
extras = {
}


# Setup boilerplate below this line.

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, 'README.rst')
with io.open(readme_filename, encoding='utf-8') as readme_file:
    readme = readme_file.read()

# Only include packages under the 'google' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    package for package in setuptools.find_packages()
    if package.startswith('google')]

# Determine which namespaces are needed.
namespaces = ['google']
if 'google.cloud' in packages:
    namespaces.append('google.cloud')


setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author='Google LLC',
    author_email='googleapis-packages@google.com',
    license='Apache 2.0',
    url='https://github.com/GoogleCloudPlatform/google-cloud-python',
    classifiers=[
        release_status,
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Internet',
    ],
    platforms='Posix; MacOS X; Windows',
    packages=packages,
    namespace_packages=namespaces,
    install_requires=dependencies,
    extras_require=extras,
    include_package_data=True,
    zip_safe=False,
)
