git/ignore
=========

git ignore test

* When a file is added as an ignored file (added to .gitignore ), it wont be
automatically added to index
* Use add -f to force add it
* Once the file is indexed, git notice the change in the file
* Thus, gitignore is only referenced when adding files, and not when updating
files
