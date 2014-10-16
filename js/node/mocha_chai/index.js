#!/usr/bin/evn node

//var assert = require('assert');
var expect = require('chai').expect

describe('testest', function(){
    describe('nesttest', function(){
        expect(1+0).to.be.equal(1);

        describe('nestnesttest', function(){
            expect(1-0).to.be.equal(1);
        });

        describe('nestnestest2', function(){
            //expect(1+1).to.be.equal(1);
        });
});
});

