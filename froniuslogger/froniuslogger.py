#!/usr/bin/env python

from os.path import dirname

from util import get_data_from_api, get_configuration

here = dirname(__file__)

import requests
from pprint import pprint

if __name__ == '__main__':
    api_version, base_url, api_path = get_configuration()
    data = get_data_from_api(api_path, 'foobardata')

    pprint(requests.get(api_path))
    print api_version
    print base_url
    print api_path
