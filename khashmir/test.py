﻿# The contents of this file are subject to the BitTorrent Open Source License
# Version 1.1 (the License).  You may not copy or use this file, in either
# source code or executable form, except in compliance with the License.  You
# may obtain a copy of the License at http://www.bittorrent.com/license/.
#
# Software distributed under the License is distributed on an AS IS basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.  See the License
# for the specific language governing rights and limitations under the
# License.

import unittest

import ktable, khashmir
import khash, node, knode
import actions
import test_krpc
import test_khashmir
import kstore

tests = unittest.defaultTestLoader.loadTestsFromNames(['kstore', 'khash', 'node', 'knode', 'actions',  'ktable', 'test_krpc', 'test_khashmir'])
result = unittest.TextTestRunner().run(tests)
