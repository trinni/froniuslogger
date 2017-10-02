# -*- coding: utf-8 -*-

import requests
import types
import urllib
import urlparse


class BaseAgent(object):
    def __init__(self, host_address):
        self.info_url = urlparse.urljoin(host_address, "solar_api/GetAPIVersion.cgi")
        self.info_response = requests.get(self.info_url)
        self.info = None
        # Default values according to Fronius Solar API v1, 2.3.1, Listing 3
        self.api_version = 0
        self.base_url = '/solar_api/'

        if self.info_response.status_code != 404:
            self.info = self.info_response.json()
            if u'APIVersion' in self.info:
                self.api_version = self.info[u'APIVersion']
            if u'BaseURL' in self.info:
                self.base_url = self.info[u'BaseURL']
        self.api_path = urlparse.urljoin(host_address, self.base_url)
        self.api_url = urlparse.urljoin(self.api_path, self.endpoint_name)

    @property
    def endpoint_name(self):
        return 'GetAPIVersion.cgi'

    def get_response(self, parameters=None):
        request_url = self._make_request_url(parameters)
        response = requests.get(self.api_url)
        assert response.status_code == 200
        return response.json()

    def _make_request_url(self, parameters=None):
        request_url = self.api_url
        if parameters and isinstance(parameters, types.DictType):
            request_url = request_url+'?'
            request_url = urllib.urlencode(parameters)
        return request_url