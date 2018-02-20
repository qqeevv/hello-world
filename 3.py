# -*- coding: UTF-8 -*-

import urllib.request
import urllib.parse
import json

repeat = 1
while repeat == 1 :
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i'] = input("Please type what you want to translate:")
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1512442744676'
    data['sign'] = '7f253658d7f8e3338edabe1758620e1a'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'

    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    result = target['translateResult'][0][0]['tgt']
    print('The answer is:%s' % (target['translateResult'][0][0]['tgt']))