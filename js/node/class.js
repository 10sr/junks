#!/usr/bin/env node

var AClass = function(arg1){
    this.attr1 = arg1 || "abc";
    console.log("AClass initialized");
    console.log(this);
    return this;
};

AClass.prototype.met1 = function(arg1){
    return "" + this.attr1 + ":" + (arg1 || "def");
}

var a = new AClass();
var b = new AClass("aaa");

console.log("a.met1():" + a.met1());
console.log("b.met1():" + b.met1());

a.attr1 = "bbb";

console.log("a.met1():" + a.met1());
console.log("b.met1():" + b.met1());
