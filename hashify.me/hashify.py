#!/usr/bin/env python3

bitly_id = "10sr"
bitly_key = "04de229d920d8088e09a7383b9a5323e61a251d2"

HASHIFY_URL = "http://hashify.me"
BITLY_API_HOST = "api-ssl.bitly.com"

import sys

def bitly(url):
    assert bitly_id
    assert bitly_key

    # import http.client
    import urllib.parse, urllib.request
    import json

    params = urllib.parse.urlencode({
        "longUrl" : url,
        "domain" : "j.mp",
        "access_token" : bitly_key
    })
    # headers = {"Content-type": "application/x-www-form-urlencoded",
    #            "Accept": "text/plain"}

    # i wont use HTTPConnection any more
    # conn = http.client.HTTPSConnection(BITLY_API_HOST)
    # print(params)
    # conn.request("GET", "/v3/shorten", "access_token=aa", headers)

    url = "https://{host}{path}?{params}".format(host=BITLY_API_HOST,
                                                path="/v3/shorten",
                                                params=params)
    res = urllib.request.urlopen(url)
    assert res.status == 200
    resbody = json.loads(res.read().decode("utf-8"))
    assert resbody["status_code"] == 200
    return resbody["data"]["url"]

def hashify(infile=sys.stdin):
    s = infile.read()
    b = s.encode("utf-8")

    from base64 import b64encode
    result_url = HASHIFY_URL + "/" + b64encode(b).decode("utf-8")
    return result_url

def main(argv):
    if len(argv) > 1:
        with open(argv[1]) as f:
            result = hashify(f)
    else:
        result = hashify(sys.stdin)

    if bitly_id and bitly_key:
        result = bitly(result)
    print(result)

if __name__ == "__main__":
    main(sys.argv)
