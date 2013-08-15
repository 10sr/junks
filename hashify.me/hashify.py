#!/usr/bin/env python3

bitly_id = "10sr"
bitly_key = "04de229d920d8088e09a7383b9a5323e61a251d2"

HASHIFY_URL = "http://hashify.me"
BITLY_API_HOST = "api-ssl.bitly.com"

import sys

def bitly(url):
    assert bitly_id
    assert bitly_key

    import http.client, urllib.parse
    Import json

    params = urllib.parse.urlencode({"access_token" : bitly_key,
                                     "longUrl" : url,
                                     "domain" : "j.mp"})
    # headers = {"Content-type": "application/x-www-form-urlencoded",
    #            "Accept": "text/plain"}
    headers = {"Accept": "text/plain"}

    conn = http.client.HTTPSConnection(BITLY_API_HOST)
    conn.request("GET", "/v3/shorten", params, headers)
    res = conn.getresponse()
    res = res.read()
    return res

def hashify(infile=sys.stdin):
    s = infile.read()
    b = s.encode("utf-8")

    from base64 import b64encode
    result_url = HASHIFY_URL + "/" + b64encode(b).decode("utf-8")
    print(result_url)
    return result_url

def main(argv):
    result = hashify(sys.stdin)
    if bitly_id and bitly_key:
        result = bitly(result)
    print(result)

if __name__ == "__main__":
    main(sys.argv)
