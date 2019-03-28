#!/usr/bin/env python3.6
import platform
import os
import sys
from pathlib import Path

# rst2md /home/gcharang/gitrepos/temp/setup-electrumX-server.rst > /home/gcharang/gitrepos/temp/setup-electrumX-server.md

for (dirname, dirs, filenames) in os.walk('.'):
    for filename in filenames:
        if ".rst" in filename:
            currPath = "/home/gcharang/gitrepos/Documentation/docs/source" + \
                os.path.join(dirname, filename).lstrip(".")
            destPath = "/home/gcharang/gitrepos/Documentation.md/" + \
                os.path.join(dirname, filename).lstrip(".")
            destPath = destPath.rstrip(".rst")+".md"
            os.system("rst2md "+currPath+">"+destPath)
