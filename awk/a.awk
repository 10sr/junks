#!/usr/bin/env gawk -f
BEGIN {
    RS = "";
    FS = ",";
    OFS = ":";
}

{
    print "Start"
    print $1
    print $2
    print $3
    # \n is always used for column separator
    print $4

}
