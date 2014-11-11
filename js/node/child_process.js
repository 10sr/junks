#!/usr/bin/env node

var spawn = require('child_process').spawn;

var async = require('async');


function try1(done){
    console.log('try1');
    var proc = spawn('ls', ['-a', '-l']);
    var out = '';

    proc.stdout.on('data', function(data){
        console.log('data start: ' + data + ' :data end');
        out += data;
    });
    proc.on('close', function(){
        console.log('close of try1: ' + out);
        done();
    });
}

function try2(done){
    console.log('try2');
    var proc = spawn('ls', ['-a', '-l']);
    var out = '';

    proc.stdout.on('readable', function(){
        var chunk;
        while ((chunk = proc.stdout.read()) !== null) {
            console.log('chunk: ' + chunk + ' :data end');
            out += chunk;
        }
    });
    proc.on('close', function(){
        console.log('close of try2: ' + out);
        done();
    });
}

async.series([try1, try2]);
