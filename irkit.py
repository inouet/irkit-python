#!/usr/bin/env python
# coding: utf-8

import requests
import json


class IRKitInternetAPI:
    endpoint = 'https://api.getirkit.com/1'
    clientkey = ''
    deviceid = ''

    def __init__(self, clientkey, deviceid):
        self.clientkey = clientkey
        self.deviceid = deviceid

    def get_messages(self):
        params = {
            'clientkey': self.clientkey,
        }

        headers = {'X-Requested-With': 'irkit-python'}
        url = self.endpoint + '/messages'

        r = requests.get(url, headers=headers, params=params)

        if r.status_code == 200:
            return r.json()

    def post_messages(self, data):
        message = {
            'format': 'raw',
            'freq': 38,
            'data': data
        }
        message = json.dumps(message)

        params = {
            'clientkey': self.clientkey,
            'deviceid': self.deviceid,
            'message': message
        }

        url = self.endpoint + '/messages'
        headers = {'X-Requested-With': 'irkit-python'}
        r = requests.post(url, headers=headers, params=params)
