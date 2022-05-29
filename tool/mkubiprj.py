#!/usr/bin/python

import os
import sys
import glob
import shutil

version_string = "03.01.00"

def print_help():
    print("===============================================================================")
    print("Version: %s" %(version_string))
    print("")
    print("Usage:")
    print("    python %s <base project name> (<new project name> (<branch> (<repobase>)))" % (sys.argv[0]))
    print("        ex: python %s ubiworks" % (sys.argv[0]))
    print("")
    print("    python %s --edu-clone <base project name in edu repo> (<new project name>)" % (sys.argv[0]))
    print("        ex: python %s --edu-clone mp_course_knu2022_1_2001000001_slblue" % (sys.argv[0]))
    print("")
    print("    python %s --local-clone <source project name> <destination project name>" % (sys.argv[0]))
    print("        ex: python %s --local-clone ubiworks myworks" % (sys.argv[0]))
    print("")
    print("    Base Projects")
    print("        * ubiworks: Project with all libraries")
    print("")
    print("===============================================================================")

def copy_tree(src, dst):
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.split(src)[1])
    shutil.copytree(src, dst)

def rename_contents(basename, newname):
    if basename == "" or basename == newname :
        return

    dlist = ["app", "app/%s" % basename, "source", "make", ".settings"]
    flist = []
    for dname in dlist:
        flist += glob.glob("./%s/*" % dname)
    flist += glob.glob("./.project")
    flist += glob.glob("./.cproject")
    # print(flist)
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
    # print(flist)
    for fname in flist:
        fname2 = fname.replace(basename, newname, 1)
        cmd = ("git mv %s %s" %(fname, fname2))
        print(cmd)
        os.system(cmd)
    print("")

    flist = glob.glob("./app/%s/%s*" % (newname, basename))
    # print(flist)
    for fname in flist:
        fname2 = fname.replace(basename, newname, 1)
        cmd = ("git mv %s %s" %(fname, fname2))
        print(cmd)
        os.system(cmd)
    print("")

def make_prj(basename, newname, branch, repobase = "https://github.com/ubinos", remote_rename=True):
    print("make %s from %s" % (newname, basename))

    if newname == "":
        newname = basename

    cmd = ("git clone %s/%s.git %s" % (repobase, basename, newname))
    print(cmd)
    os.system(cmd)
    os.chdir(newname)
    print("")

    if "" != branch:
        cmd = ("git checkout -b %s origin/%s" % (branch, branch))
        print(cmd)
        os.system(cmd)
        print("")

    # cmd = ("git checkout -b myprj")
    # print(cmd)
    # os.system(cmd)
    # print("")

    rename_contents(basename, newname)

    cmd = "git submodule init"
    print(cmd)
    os.system(cmd)
    cmd = "git submodule update"
    print(cmd)
    os.system(cmd)
    print("")

    if remote_rename:
        cmd = "git remote rename origin ubinos"
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

    print("successed")
    return

def local_clone(src, dst):
    print("local_clone %s to %s" % (src, dst))

    if src == "" or src == dst:
        print("failed")
        return

    copy_tree(src, dst)
    os.chdir(dst)
    rename_contents(src, dst)

    print("successed")
    return

if __name__ == '__main__':
    if 2 <= len(sys.argv) and sys.argv[1] == "--local-clone":
        if 4 == len(sys.argv):
            local_clone(sys.argv[2], sys.argv[3])
        else:
            print_help()
    elif 2 <= len(sys.argv) and sys.argv[1] == "--edu-clone":
        if 3 == len(sys.argv):
            make_prj(sys.argv[2], sys.argv[2], "master", "git@github.com:ubinos-edu", False)
        elif 4 == len(sys.argv):
            make_prj(sys.argv[2], sys.argv[3], "master", "git@github.com:ubinos-edu", False)
        else:
            print_help()
    else:
        if 2 == len(sys.argv):
            make_prj(sys.argv[1], "", "")
        elif 3 == len(sys.argv):
            make_prj(sys.argv[1], sys.argv[2], "")
        elif 4 == len(sys.argv):
            make_prj(sys.argv[1], sys.argv[2], sys.argv[3])
        elif 5 == len(sys.argv):
            make_prj(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print_help()

