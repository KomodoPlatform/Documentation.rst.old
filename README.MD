# README!

Documentation for https://docs.komodoplatform.com/
-----

This documentation is being written using the reStructuredText(reST, .rst) format. To be hosted at https://docs.komodoplatform.com/en/latest/ with the theme sphinx_rtd.

-----
To suggest edits, fork this repo, edit your fork and submit a PR
-----
To get started,

```bash
pip install sphinx sphinx-autobuild
pip install --user sphinx_rtd_theme
```
`cd` to a directory where you want to clone this project.

```bash
git clone https://github.com/gcharang/KomodoPlatformdocs.git
```
Add images to be used in the directory: docs/source/_static/images/

The content of the documentation is in: docs/source/*.rst files

To edit a document go to the appropriately named .rst file and make the changes.

To add a new document add a new .rst file in the directory docs/source/ (or create an appropriately named sub-directory) and add the name of the file (along with it's path relative to the position of index.rst) to index.rst

index.rst keeps track of all the other files and is used to build the table of contents.

Make changes to conf.py to change the configuration with which the html or pdf are to be built.

To buld the html or pdf from the source files:

`cd` to the directory docs/ 

It should contain: source/ , Makefile, make.bat

```bash
make html
make latexpdf
```
pdf will be built only if you already have texlive installed natively on your system.

The build files can be found at

docs/build/html	for html

docs/buld/latex for pdf 

To view the html as if it is hosted, `cd` into docs/build/html and do

```bash
python -m SimpleHTTPServer
```
--------------------------

A quick intro/cheat-sheet for reST: http://docutils.sourceforge.net/docs/user/rst/quickref.html

A bit more elaborate and also has sphinx specific syntax: https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html

Another sphinx reference: http://rest-sphinx-memo.readthedocs.io/en/latest/Sphinx.html

reST Syntax Reminders: https://gist.github.com/ionelmc/e876b73e2001acd2140f

---------------------------

.gitignore ignores the build directory.

