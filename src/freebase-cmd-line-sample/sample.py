# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Command-line skeleton application for Freebase Search.
Usage:
  $ python sample.py

You can also get help on all the command-line flags the program understands
by running:

  $ python sample.py --help

"""

import httplib2
import sys

from apiclient import discovery


def main(argv):
  # Create an httplib2.Http object to handle our HTTP requests .
  http = httplib2.Http()

  # Construct the service object for the interacting with the Freebase Search.
  service = discovery.build('freebase', 'v1',  developerKey='', http=http)

  print "Success! Now add code here."

  return service


# For more information on the Freebase Search you can visit:
#
#   https://developers.google.com/freebase/
#
# For more information on the Freebase Search Python library surface you
# can visit:
#
#   https://developers.google.com/resources/api-libraries/documentation/freebase/v1/python/latest/
#
# For information on the Python Client Library visit:
#
#   https://developers.google.com/api-client-library/python/start/get_started
if __name__ == '__main__':
  main(sys.argv)
