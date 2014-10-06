#!/usr/bin/env node
// myhttp.js
// http://www.nodebeginner.org/index-jp.html

var http = require('http');
var url = require('url');

function onReqWOListener(req, res) {
    var pathname = url.parse(req.url).pathname;
    console.log("Request for " + pathname + " Recieved!");
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hell, World\n');
}

// not work with GET?
function onReqWithListener(req, res) {
    req.addListener("end", function(){
        var pathname = url.parse(req.url).pathname;
        console.log("Request for " + pathname + " Recieved!");
        res.writeHead(200, {'Content-Type': 'text/plain'});
        res.end('Hell, World\n');
    });
}

http.createServer(onReqWOListener).listen(1337, '192.168.56.101');

console.log('Server running at http://192.168.56.101:1337');
