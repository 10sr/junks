EditorConfig Example
=====================


Example File
-------------

This sample is from [the official page](http://editorconfig.org/#example-file).


```
# EditorConfig is awesome: http://EditorConfig.org

# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
end_of_line = lf
insert_final_newline = true

# Matches multiple files with brace expansion notation
# Set default charset
[*.{js,py}]
charset = utf-8

# 4 space indentation
[*.py]
indent_style = space
indent_size = 4

# Tab indentation (no size specified)
[*.js]
indent_style = tab

# Indentation override for all JS under lib directory
[lib/**.js]
indent_style = space
indent_size = 2

# Matches the exact files either package.json or .travis.yml
[{package.json,.travis.yml}]
indent_style = space
indent_size = 2
```



Output of EditorConfig
-----------------------

`make ed` to print properties for `a.c`

```
fuafua=2
indent_style=tab
indent_size=4
hoehoe=1
tab_width=4
```


It means that:

* Basically the order of properties will be preserved
* Even when some properties is overwritten, the order will not change:
  only updating the values
* `tab_width` properties will be automatically appended at the end
  if `indent_style=tab` (?)
