README!

Documentation for https://komodo-platform.readthedocs.io/
-----

This documentation is being written using the Restructured Text(reST, .rst) format. To be hosted at http://komodoplatform.readthedocs.io/en/latest/ with the theme sphinx_rtd.

-----
To suggest edits, fork this repo, edit your fork and submit a PR
-----
To get started,

```bash
pip install sphinx sphinx-autobuild
```
`cd` to a directory where you want to clone this project.

```bash
git clone https://github.com/gcharang/KomodoPlatformdocs.git
```
Add images to be used in the directory: docs/source/_static/images/

The content of the document is in: docs/source/*.rst files

To edit a section go to the appropriately named .rst file and make the changes.

To add a new section add a new .rst file to the directory docs/source/ and add the name of the file to index.rst

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

