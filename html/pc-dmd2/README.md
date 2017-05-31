Dynamic Markdown loader (dmd.js)
=======================

If javascript is enabled, dmd.js automatically collect contents in the page with
their titles and create a menu that references these contents.
These contents are written in markdown and are converted with `marked()` when
displayed.

If javascript is not enabled, contents are available as `pre`ed markdown texts
or links to external files.


Elements
--------


### #dmd-content

When you are constructing a source, this element should has as children elements
who have classes `"dmd-page"` and `title` attributes.
Currently `pre` and `a` elements are allowed for these children.
Values of `title` attributes are used for names of links and hashes.
`title`s must be unique in these children (otherwise latter one overwrites
former one).

If javascript works, when loading the page all children of this element (not
only `pre` and `a` elements) are removed.
When the hash changes the content whose title is specified by the hash is
`marked()` and added as the child of this element.


### ul#dmd-menu

If this element exists and javascript works, `li` elements each of who has an
`a` element referencing hash + `title` are appended.
