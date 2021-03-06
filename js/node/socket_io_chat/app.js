// http://www.tettori.net/post/852/

var http = require('http');
var socketio = require('socket.io');
var fs = require('fs');

var server = http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type': 'text/html'});
    var output = fs.readFileSync('./index.html', 'utf-8');
    res.end(output);
}).listen(3000);

var io = socketio.listen(server);

io.sockets.on('connection', function(socket){

    // custom event
    socket.on('C_to_S_message', function(data){
        // all including the client sent the message
        io.sockets.emit('S_to_C_message', {value: data.value});
    });

    // custom event
    socket.on('C_to_S_broadcast', function(data){
        // all except the client (use obj passed throug arg of io.sockets.on)
        socket.broadcast.emit('S_to_C_message', {value: data.value});
    });

    socket.on('disconnect', function(){
        console.log('client disconnected');
    });
});


console.log('Server running at http://127.0.0.1:3000');
