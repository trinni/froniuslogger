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
    def __init__(self, response, msg):
        self.value = response
        self.message = msg

    def __str__(self):
        return 'Error in retrieved response: {}\n Response was: {}'.format(
            self.message, self.value)
