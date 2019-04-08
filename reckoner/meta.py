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
from pkg_resources import get_distribution
import re

__version_modifier__ = re.compile(r'^([0-9]+\.[0-9]+\.[0-9]+)\.(.*)$')
__distribution_name__ = 'reckoner'
__version__ = re.sub(__version_modifier__, r'\g<1>-\g<2>', get_distribution(__distribution_name__).version)
__author__ = 'ReactiveOps, Inc.'
