var http = require('http');
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hell, World\n');
}).listen(1337, '192.168.56.101');
console.log('Server running at http://192.168.56.101:1337');
