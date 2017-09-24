# -*- coding: utf-8 -*-
from froniuslogger.exceptions import UnknownFroniusDataType
from froniuslogger.util import get_configuration, get_data_from_api
from unittest2 import TestCase

from froniuslogger import settings


class TestAPIVersion(TestCase):
    def testSupportedVersionConfiguredAsExpected(self):
        self.assertEquals(settings.APIVersion, 1)


class TestDataTypeMappings(TestCase):
    def test_unknown_datatype(self):
        api_version, base_url, api_path = get_configuration()
        self.assertRaises(UnknownFroniusDataType, get_data_from_api(api_path, 'some_unknown_datatype'))
