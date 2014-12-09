#!/usr/bin/env node

var async = require('async');

var tasks = [];

tasks.push(function(done){
  console.log('First tasks called');
  done(new Error('error of first task'), 0);
});

tasks.push(function(done){
  console.log('Second tasks called');
  done(new Error('error of second task'), 1);
});

async.parallel(tasks, function(err, results){
  console.log(err); // [Error: error of first task]
  console.log(results); // [ 0 ]
});
