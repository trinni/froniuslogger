# -*- coding: utf-8 -*-

class UnknownFroniusDataType(BaseException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Fronius Data Type unknown: "{}"'.format(self.value)


class UnknownFroniusEndpoint(BaseException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Fronius Endpoint not known: "{}"'.format(self.value)


class ResponseIsBad(BaseException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Response status is bad, either the statuscode was bad or it could not be found in response. Response was: {}'.format(
            self.value)
