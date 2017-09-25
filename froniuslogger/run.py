#!/usr/bin/env python

from os.path import dirname
import settings
from froniuslogger.agents.InverterRealtimeDataAgent import InverterRealtimeDataAgent
from froniuslogger.lib.util import get_configuration
from pprint import pprint
here = dirname(__file__)

import requests

if __name__ == '__main__':
    api_version, base_url, api_path = get_configuration()
    agent = InverterRealtimeDataAgent(settings.fronius_baseurl)
    response = agent.get_response({'Scope': 'Device', 'DataCollection': 'MinMaxInverterData', 'DeviceId': 1})

    pprint(response)
    print api_version
    print base_url
    print api_path
