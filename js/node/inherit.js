#!/usr/bin/env node

// http://nodejs.jp/nodejs.org_ja/api/util.html#util_util_inherits_constructor_superconstructor

var inherits = require('util').inherits;

var AClass = function(){
    this.a1 = 'ab';
};

AClass.prototype.m1 = function(arg1, arg2){
    console.log([this.a1, arg1, arg2].join(':'));
};

var a = new AClass();
a.m1('222', '444');

// inherit aclass to make bclass

var BClass = function(){
    AClass.call(this);
};

inherits(BClass, AClass);

BClass.prototype.m2 = function(){
    console.log('bclass.m2');
    this.m1('cccc', '8888');
};

var b = new BClass();
b.m2();

// add instance as a object member
// http://taiju.hatenablog.com/entry/20100515/1273903873

var CClass = function(){
    this.a = new AClass();
};

CClass.prototype.m1 = function(arg1, arg2){
    // arguments[0] === arg1, arguments[1] === arg2
    console.log(arguments);
    // call this.a.m1
    this.a.m1.apply(this.a, arguments);
};

var c = new CClass();
c.m1("abc", "def");
