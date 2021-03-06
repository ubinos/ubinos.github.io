#!/usr/bin/python

import os
import sys
import glob

def print_help():
    print("===============================================================================")
    print("Usage:")
    print("    python %s <base project name> <new project name>" % (sys.argv[0]))
    print("        ex: python %s ex01 myapp01" % (sys.argv[0]))
    print("")
    print("    Base Projects")
    print("        * ex01: Basic Example for All Boards")
    print("        * ex02nrf5: Basic Example for nRF5 Family Boards")
    print("        * ex03stm32f2: Basic Example for STM32F2 Family Boards")
    print("")
    print("===============================================================================")

def mkubiprj(basename, newname, repobase):
    if "" == repobase:
        repobase = "https://github.com/ubinos"
        
    cmd = ("git clone %s/%s.git %s" % (repobase, basename, newname))
    print(cmd)
    os.system(cmd)
    os.chdir(newname)
    print("")

    dlist = ["app", "source", "make"]
    for dname in dlist:
        flist = glob.glob("./%s/*" % dname)
        for fname in flist:
            if (os.path.isdir(fname)):
                continue
            print("modify %s" % fname)
            fin = open(fname, "rt")
            data = fin.read()
            data = data.replace(basename, newname)
            fin.close()
            fin = open(fname, "wt")
            fin.write(data)
            fin.close()
    print("")
    
    flist = glob.glob("./app/%s*" % basename)
    for fname in flist:
        fname2 = fname.replace(basename, newname, 1)
        cmd = ("git mv %s %s" %(fname, fname2))
        print(cmd)
        os.system(cmd)
    print("")

    cmd = "git submodule init"
    print(cmd)
    os.system(cmd)
    cmd = "git submodule update"
    print(cmd)
    os.system(cmd)
    print("")

    cmd = "git remote remove origin"
    print(cmd)
    os.system(cmd)
    print("")

    cmd = "git add ."
    print(cmd)
    os.system(cmd)
    print("")

    #cmd = ("git commit -m \"Create project \\\"%s\\\" based on \\\"%s\\\"\"" %(newname, basename))
    #print(cmd)
    #os.system(cmd)
    #print("")

if __name__ == '__main__':
    if 3 == len(sys.argv):
        mkubiprj(sys.argv[1], sys.argv[2], "")
    elif 4 == len(sys.argv):
        mkubiprj(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print_help()

