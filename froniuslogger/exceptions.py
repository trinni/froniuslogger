# -*- coding: utf-8 -*-

class UnknownFroniusDataType(BaseException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Fronius Data Type unknown: "{}"'.format(self.value)
