#!/usr/bin/env node

var webshot = require('webshot');

function main(){
  webshot('http://tokyo-ame.jwa.or.jp/', 'cap.png', function(err){
    console.error(err);
  })
}

main();
