#!/usr/bin/env node

function makeNewObj(){
    var o = {};
    o.key = 'value';
    return o;
}

var o1 = makeNewObj();
var o2 = makeNewObj();

console.log(o1 === o2);
