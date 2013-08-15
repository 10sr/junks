hashify.py
==========

Python client for [hashify.me](http://hashify.me) service.

Developed by [10sr](https://github.com/10sr), at
<https://github.com/10sr/junks/tree/master/hashify.me> .



Usage
=====

    $ hashify [<filename>]

If a filename is given, read contents from that file. Otherwise, contents is
read from stdin. Bitly-shortened URL will be printed out.


bit.ly
======

By default, my (10sr) account is used for shorten URLs.
You can use your own access token if you want. Your access token is available
at <https://bitly.com/a/oauth_apps> .
