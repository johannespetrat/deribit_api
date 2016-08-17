import requests
import json
import hashlib
import base64
import datetime

KEY = YOUR ACCESS KEY
SECRET= YOUT ACCESS SECRET

def get_instruments():
    url = 'https://deribit.com/api/v1/public/getinstruments'
    response = requests.get(url)
    return json.loads(response.text)

def get_index():
    url = 'https://deribit.com/api/v1/public/index'
    response = requests.get(url)
    return json.loads(response.text)

def get_currencies():
    url = 'https://deribit.com/api/v1/public/getcurrencies'
    response = requests.get(url)
    return json.loads(response.text)

def get_orderbook(instrument):
    url = 'https://deribit.com/api/v1/public/getorderbook?instrument='+instrument
    response = requests.get(url)
    return json.loads(response.text)

def get_lasttrades(instrument):
    url = 'https://deribit.com/api/v1/public/getlasttrades?instrument='+instrument
    response = requests.get(url)
    return json.loads(response.text)

def get_summary(instrument):
    url = 'https://deribit.com/api/v1/public/getsummary?instrument='+instrument
    response = requests.get(url)
    return json.loads(response.text)

def create_signature(action):
    #action = url.split('deribit.com')[1]
    ts = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds()*1000)
    path = '_='+str(ts)+'&_ackey='+KEY+\
            '&_acsec='+SECRET+\
            '&_action='+action
    hashed = hashlib.sha256(path)
    bs64_hash = base64.encodestring(hashed.digest())[:-1]
    signature = '.'.join([KEY,str(ts),bs64_hash])
    return signature

def account():
    url = 'https://deribit.com/api/v1/private/account'
    action = url.split('deribit.com')[1]
    #action = URI Path&param1=value1&param2=value2….&paramN=valueN’
    signature = create_signature(action)
    req = urllib2.Request(url)
    req.add_header('x-deribit-sig', signature)
    response = urllib2.urlopen(req)
    return json.loads(response.read())


#def sell(instrument, quantity, price):
def sell():
    instrument = "BTC-12AUG16-520-C"
    quantity = "1"
    price = "12"
    url = 'https://test.deribit.com/api/v1/private/sell?instrument='+instrument+\
                '?price='+price+'?quantity='+quantity
    #action = url.split('deribit.com')[1]
    action = '/api/v1/private/sell&instrument=BTC-12AUG16-520-C&price=12&quantity=1'
    #action = URI Path&param1=value1&param2=value2….&paramN=valueN’
    signature = create_signature(action)
    req = urllib2.Request(url)
    req.add_header('x-deribit-sig', signature)
    response = urllib2.urlopen(req)
    return json.loads(response.read())

def get_openorders():
    url = 'https://deribit.com/api/v1/private/getopenorders'
    action = '/api/v1/private/getopenorders'
    signature = create_signature(action)
    req = urllib2.Request(url)
    req.add_header('x-deribit-sig', signature)
    response = urllib2.urlopen(req)
    return json.loads(response.read())

def get_positions():
    url = 'https://deribit.com/api/v1/private/positions'
    action = '/api/v1/private/positions'
    signature = create_signature(action)
    req = urllib2.Request(url)
    req.add_header('x-deribit-sig', signature)
    response = urllib2.urlopen(req)
    return json.loads(response.read())


if __name__ == "__main__":
    print '###' * 20
    print "get_instruments() "
    print '###' * 20
    print get_instruments()
    print '###' * 20
    print "get_index()"
    print '###' * 20
    print get_index()
    print '###' * 20
    print "get_currencies()"
    print '###' * 20
    print get_currencies()

    instrument_name = 'BTC-5AUG16-620-P'
    print '###' * 20
    print "get_orderbook()"
    print '###' * 20
    print get_orderbook(instrument_name)
    print '###' * 20
    print "get_lasttrades()"
    print '###' * 20
    print get_lasttrades(instrument_name)
    print '###' * 20
    print "get_summary()"
    print '###' * 20
    print get_summary(instrument_name)
