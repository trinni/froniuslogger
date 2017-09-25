# -*- coding: utf-8 -*-

from unittest2 import TestCase

from froniuslogger.exceptions import UnknownFroniusEndpoint, ResponseIsBad
from froniuslogger.lib import util
from froniuslogger.lib.util import get_configuration, get_json_by_url
from froniuslogger.settings import APIVersion


class TestAPIVersion(TestCase):
    def testSupportedVersionConfiguredAsExpected(self):
        self.assertEquals(APIVersion, 1)


class TestEndpoint(TestCase):
    def testUnknonwnEndpointFails(self):
        api_version, base_url, api_path = get_configuration()
        with self.assertRaises(UnknownFroniusEndpoint):
            endpoint_url = util.get_endpoint_url('GetInverterRealtimeDat.cgi')
            get_json_by_url(endpoint_url)

    def testIncompleteParametersFails(self):
        api_version, base_url, api_path = get_configuration()
        endpoint_url = util.get_endpoint_url('GetInverterRealtimeData.cgi')
        with self.assertRaises(ResponseIsBad):
            json = get_json_by_url(endpoint_url)

