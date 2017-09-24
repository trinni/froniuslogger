# -*- coding: utf-8 -*-
import requests
import urlparse

from froniuslogger.exceptions import UnknownFroniusDataType
from froniuslogger.settings import Settings


def parse_info_json(info_json):
    infos = info_json.json()
    return (int(infos[u'APIVersion']), infos[u'BaseURL'])


def get_configuration():
    info_url = urlparse.urljoin(Settings.fronius_baseurl, "solar_api/GetAPIVersion.cgi")
    info_json = requests.get(info_url)

    # According to Fronius Solar API v1, 2.3.1, Listing 3
    if info_json.status_code == 404:
        api_version = 0
        base_url = '/solar_api/'

    api_version, base_url = parse_info_json(info_json)
    assert api_version == Settings.APIVersion

    api_path = urlparse.urljoin(Settings.fronius_baseurl, base_url)
    return api_version, base_url, api_path


def get_data_type_mappings():
    data_type_mappings = {'inverter_realtime_data': 'GetInverterRealtimeData.cgi'}
    return data_type_mappings


def get_data_from_api(api_path, fronius_data_type):
    data_type_mappings = get_data_type_mappings()
    if fronius_data_type not in data_type_mappings:
        raise UnknownFroniusDataType(fronius_data_type)
    data_url = urlparse.urljoin(api_path, data_type_mappings[fronius_data_type])
    response = requests.get(data_url)
    assert response.status_code == 200
    return response.json()
