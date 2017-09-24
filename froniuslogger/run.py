#!/usr/bin/env python

from os.path import dirname

from froniuslogger.lib.util import get_configuration, get_data_from_api

here = dirname(__file__)

import requests
from pprint import pprint

if __name__ == '__main__':
    api_version, base_url, api_path = get_configuration()
    data = get_data_from_api(api_path, 'inverter_realtime_data')

    pprint(requests.get(api_path))
    print api_version
    print base_url
    print api_path
