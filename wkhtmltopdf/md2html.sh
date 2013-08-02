#!/bin/sh

markdown=`which markdown 2>/dev/null`
if test -z "$markdown"
then
    echo "$0: markdown not installed" 1>&2
    echo "Abort" 1>&2
    exit 1
fi

if test $# -eq 0
then
    exec 3<&0
else
    exec 3<<__EOC__
`cat "$@"`
__EOC__
fi

cat <<'__EOC__'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link href="style.css" rel="stylesheet" type="text/css" />
    <link href="slide.css" rel="stylesheet" type="text/css" />
    <title>main</title>
  </head>
  <body class="content">
__EOC__

"$markdown" 0<&3

cat <<'__EOC__'
</body>
</html>
__EOC__

exec 3<&-
