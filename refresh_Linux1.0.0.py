/*This program is about to use as enhance utility & user friendly access on LINUX systems. This script does nothing but refresh the */
/* APP_STACK with respect to the man_DB in the host SYSTEM. In this prototype program only utility is enhanced. No GUI effect is included*/
/* into this at all. If the LIB bassed on PYTHON 2.x supports OpenGL then it would work on next update.

#!/usr/bin/env python
#Usage:This program consists for 'Clean-up Program using Python'

import pygtk
pygtk.require('2.0')
import gtk
import os

def check(path):
    """Returns true to indicate a file should be removed."""
    
    if path.endswith('~'):
        return True
    if path.startswith('#') and basename.endswith('#'):
        return True
    if path.endswith('.pyc'):
        return True
    return False

def walk(dirname=None):
    selected = os.environ.get('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS', '')
    curdir = os.environ.get('NAUTILUS_SCRIPT_CURRENT_URI', os.curdir)
    
    if dirname is not None:
        targets = [dirname]
    elif selected:
        targets = selected.splitlines()
    else:
        targets = [curdir]
    
    for target in targets:
        if target.startswith('file:///'):
            target = target[7:]
        if not os.path.isdir(target): continue
        for dirname, dirnames, files in os.walk(target):
            for dir in dirnames:
                dir = os.path.join(dirname, dir)
                walk(dir)
            for file in files:
                file = os.path.join(dirname, file)
                if check(file):
                    os.remove(file)

if __name__ == '__main__':
    walk()
