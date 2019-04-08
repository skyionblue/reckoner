# -- coding: utf-8 --

# pylint: skip-file

# Copyright 2019 ReactiveOps Inc
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
from setuptools_scm import get_version
import re

__version_modifier__ = re.compile(r'^([0-9]+\.[0-9]+\.[0-9]+)\.(.*)$')
__version__ = re.sub(__version_modifier__, r'\g<1>-\g<2>', get_version())
__author__ = 'ReactiveOps, Inc.'
