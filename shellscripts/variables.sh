#!/bin/bash

readonly HOE=3

f(){
    local readonly HOE=1
    echo $HOE
}

f
