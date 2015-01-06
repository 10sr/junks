#!/usr/bin/env node

var async = require('async');

var tasks = [];

// I have a question: I know that I cannot know which function finish first
// (how order done() is called), but how about the *calls* of functions?
// In this case the `console.log()`s are assured to be called in the order
// they appear???

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
