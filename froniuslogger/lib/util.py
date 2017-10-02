# -*- coding: utf-8 -*-
import requests
import types
import urlparse
from urllib3 import request

from froniuslogger.exceptions import UnknownFroniusDataType, UnknownFroniusEndpoint, ResponseIsBad
from froniuslogger.settings import fronius_baseurl, APIVersion


def parse_info_json(info_json):
    infos = info_json.json()
    return (int(infos[u'APIVersion']), infos[u'BaseURL'])


def get_configuration():
    info_url = urlparse.urljoin(fronius_baseurl, "solar_api/GetAPIVersion.cgi")
    info_json = requests.get(info_url)

    # According to Fronius Solar API v1, 2.3.1, Listing 3
    if info_json.status_code == 404:
        api_version = 0
        base_url = '/solar_api/'

    api_version, base_url = parse_info_json(info_json)
    assert api_version == APIVersion

    api_path = urlparse.urljoin(fronius_baseurl, base_url)
    return api_version, base_url, api_path


def make_range_value_pattern_description(range_value_pattern, description):
    return {'_Range_Value_Pattern': range_value_pattern, '_Description': description}


def make_paramater_type_values(parameter, parameter_type, values):
    return {'_Parameter': parameter, '_Type': parameter_type, '_Values': values}


def get_endpoint_url(endpoint_name):
    if not endpoint_exists(endpoint_name):
        raise UnknownFroniusEndpoint(endpoint_name)
    else:
        _, _, api_path = get_configuration()
        return urlparse.urljoin(api_path, endpoint_name)


def endpoint_exists(endpoint_name):
    return endpoint_name in get_endpoint_mappings()


def get_endpoint_mappings():
    return {'GetInverterRealtimeData.cgi':
        [
            make_paramater_type_values('Scope', types.StringType,
                                       [make_range_value_pattern_description('Device', 'Query specific device'),
                                        make_range_value_pattern_description('System', 'Query whole system')]),
            make_paramater_type_values('DeviceIndex', types.IntType, [
                make_range_value_pattern_description(n, 'Only needed for Scope "Device" which inverter to query') for n
                in range(0, 99)]),
            make_paramater_type_values('DataCollection', types.StringType,
                                       [make_range_value_pattern_description(value,
                                                                             'Only needed for Scope Device. Selected the collection of data to be queried.')
                                        for value in ['CumulationInverterData', 'CommonInverterData', '3PInverterData',
                                                      'MinMaxInverterData']])
        ]
    }


def get_endpoint_mapping(endpoint_name):
    if not endpoint_exists(endpoint_name):
        raise UnknownFroniusEndpoint(endpoint_name)
    else:
        endpoint_mappings = get_endpoint_mappings()
        return endpoint_mappings[endpoint_name]


def get_json_by_url(url):
    response = requests.get(url)
    assert response.status_code == 200

    response = response.json()
    assert_response_is_ok(response)

    return response

def assert_response_is_ok(response):
    """
    Checks whether or not response is well-formed and status code is ok
    """
    if not ('Head' in response and 'Status' in response['Head'] and 'Code'in response['Head']['Status']):
        raise ResponseIsBad(response, 'Json was malformed')
    if response['Head']['Status']['Code'] != 0:
        message = response['Head']['Status']['UserMessage']
        raise ResponseIsBad(response, message)

def extract_body_from_response(response):
    depacked = response.json
    if u'Body' in depacked:
        return depacked['Body']
    else:
        # TODO: eventually raise an exception here
        return None

    # http://192.168.2.5/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DeviceId=1&DataCollection=CommonInverterData
