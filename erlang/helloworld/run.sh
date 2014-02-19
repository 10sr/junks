#!/bin/sh

erlc hw.erl

erl -noshell -s hw start -s init stop
