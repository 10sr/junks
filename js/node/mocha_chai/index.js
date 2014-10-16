#!/usr/bin/evn node

//var assert = require('assert');
var expect = require('chai').expect

describe('testest', function(){
    describe('nesttest', function(){
        it('should be 1', function(){
            expect(1+0).to.be.equal(1);
        });
    });

    describe('nestnesttest', function(){
        it('should be 1 #2', function(){
            expect(1-0).to.be.equal(1);
        });

        describe('nestnestest2', function(){
            it('(fail) should be 1 #3', function(){
                expect(1-1).to.be.equal(1);
            });
        });
    });
});

