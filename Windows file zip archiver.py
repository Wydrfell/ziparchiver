#Windows file archiver
import zipfile, os, shutil, argparse, sys, calendar
from datetime import datetime

class ArgumentError(Exception):

    def __init__(self,path):
        self.path = path

    def __str__(self):
        return(repr(self.path))

def sortByOptions(src, dest, optstr):
    currdir = src
    print(optstr)
    filelist = getFiles(src)
    dirlist = getFolders(src)
    print(filelist, dirlist)
    if optstr != []:
        prevfolders = []
        for opt in optstr:
            if 'day' in opt:
                prevfolders = dayOpt(src, prevfolders)
            elif 'year' in opt:
                prevfolders = yearOpt(src, prevfolders)
            elif 'month' in opt:
                prevfolders = monthOpt(src, prevfolders)
                print("previous folders: ",prevfolders)
            elif 'file' in opt:
                prevfolders = fileOpt(src, prevfolders)
   
    #zip entire directory

    pass

def getFiles(dir):
    return next(os.walk(dir))[2]

def getFolders(dir):
    return next(os.walk(dir))[1]

def sortNmove(curfolder, folderlist):
    flist = getFiles(curfolder)
    for f in flist:
        curfile = os.path.join(curfolder, f)
        option = calendar.month_name[int(datetime.fromtimestamp(os.path.getctime(curfile)).strftime('%m'))]
        folderpath = os.path.join(curfolder, option)
        # [REMOVE]
        # datetime.fromtimestamp().strftime('%Y-%m-%d %H:%M:%S')
        print(curfile, option)
        if option not in folderlist and not os.path.exists(folderpath):
            # [REMOVE]
            print("Creating", option, "folder...")
            os.makedirs(folderpath)
            folderlist.append(option)
        shutil.move(curfile, folderpath)
    

def dayOpt(src, prevfolders):
    activefolders = prevfolders
    prevfolders = []
    pass

def yearOpt(src, prevfolders):
    activefolders = prevfolders
    prevfolders = []
    if activefolders == []:
        flist = getFiles(src)
        for f in flist:
            curfile = os.path.join(src, f)
            year = calendar.month_name[int(datetime.fromtimestamp(os.path.getctime(curfile)).strftime('%Y'))]
            folderpath = os.path.join(src, month)
            # [REMOVE]
            # datetime.fromtimestamp().strftime('%Y-%m-%d %H:%M:%S')
            print(curfile, month)
            if month not in prevfolders and not os.path.exists(folderpath):
                # [REMOVE]
                print("Creating", month, "folder...")
                os.makedirs(folderpath)
                prevfolders.append(month)
            shutil.move(curfile, folderpath)
    else:
        for folder in activefolders:
            curfolder = os.path.join(src, folder)
            flist = getFiles(curfolder)
            for f in flist:
                curfile = os.path.join(curfolder, f)
                month = calendar.month_name[int(datetime.fromtimestamp(os.path.getctime(curfile)).strftime('%m'))]
                folderpath = os.path.join(curfolder, month)
                print(curfile, month)
                if month not in prevfolders and not os.path.exists(folderpath):
                    # [REMOVE]
                    print("Creating", month, "folder...")
                    os.makedirs(folderpath)
                    prevfolders.append(month)
                shutil.move(curfile, folderpath)

    return(prevfolders)

def monthOpt(src, prevfolders):
    activefolders = prevfolders
    prevfolders = []
    if activefolders == []:
        flist = getFiles(src)
        for f in flist:
            curfile = os.path.join(src, f)
            month = calendar.month_name[int(datetime.fromtimestamp(os.path.getctime(curfile)).strftime('%m'))]
            folderpath = os.path.join(src, month)
            # [REMOVE]
            # datetime.fromtimestamp().strftime('%Y-%m-%d %H:%M:%S')
            print(curfile, month)
            if month not in prevfolders and not os.path.exists(folderpath):
                # [REMOVE]
                print("Creating", month, "folder...")
                os.makedirs(folderpath)
                prevfolders.append(month)
            shutil.move(curfile, folderpath)
    else:
        for folder in activefolders:
            curfolder = os.path.join(src, folder)
            flist = getFiles(curfolder)
            for f in flist:
                curfile = os.path.join(curfolder, f)
                month = calendar.month_name[int(datetime.fromtimestamp(os.path.getctime(curfile)).strftime('%m'))]
                folderpath = os.path.join(curfolder, month)
                print(curfile, month)
                if month not in prevfolders and not os.path.exists(folderpath):
                    # [REMOVE]
                    print("Creating", month, "folder...")
                    os.makedirs(folderpath)
                    prevfolders.append(month)
                shutil.move(curfile, folderpath)

    return(prevfolders)

def fileOpt(src, prevfolders):
    activefolders = prevfolders
    prevfolders = []
    pass

def getFilename(path):
    i = len(path)
    while path[i-1] != "\\":
        i -= 1
    return path[i:]

def setDest(src, dest):
    if dest == '':
        fname = getFilename(src)
        filedir = src.replace("\\" + fname, "")
        return(os.path.abspath(filedir))
    else:
        return(os.path.abspath(dest))

def parseOptions(argstr):
    arglist = argstr.split(" ")
    options = []
    for a in arglist:
        if a[:2] == "--":
            options.append(a)
    return options

# parse through arguments
parser = argparse.ArgumentParser(description='Archive and sort some files. List sort options in order by hierarchy.')
parser.add_argument('zip', metavar='zip', type=str, help='Zipfile Name')
parser.add_argument('src', metavar='src', type=str, help='Target File')
parser.add_argument('dest', metavar='dest', nargs = '?', type=str, default = '', help='Target Directory')
parser.add_argument('--year', action='store_true', help='sort files into folders by year')
parser.add_argument('--file', action='store_true', help='sort files into folders by file type')
parser.add_argument('--month', action='store_true', help='sort files into folders by month')
parser.add_argument('--day', action='store_true', help='sort files into folders by day')

args = parser.parse_args()

# [REMOVE] check to see the value of argument and if they were parsed correctly
print(args)
print(args.src, args.dest)

# Keep arg string as is for parsing later
argstr = ' '.join(sys.argv[1:])
# [REMOVE] print argstring
print("Arg String:",argstr)

argc = len(sys.argv)
zipname = args.zip

totalfilesize = 0
zipfilesize = 0

# check if src is file or directory if neither, Error
if not os.path.isfile(args.src):
    if not os.path.isdir(args.src):
        try:
            raise ArgumentError(args.src)
        except ArgumentError as error:
            print("Error:", error.path, "is not a valid file or directory path.")
    else:
        print("Directory Detected.")
        src = os.path.abspath(args.src)
        dest = setDest(src, args.dest)
        sortByOptions(src, dest, parseOptions(argstr))
else:
    print("File Detected.")
    print("Zipping File...")
    src = os.path.abspath(args.src)
    dest = setDest(src, args.dest)
    # create a new zipfile
    newZip = zipfile.ZipFile(zipname, 'w')
    newZip.write(src, compress_type=zipfile.ZIP_DEFLATED)
    # [REMOVE]
    print(newZip.namelist())
    # grab zipfile information
    zipInfo = newZip.getinfo(newZip.namelist()[0])
    totalfilesize += zipInfo.file_size
    zipfilesize += zipInfo.compress_size
    # [REMOVE]
    print("og file:", totalfilesize, "\ncompressed:", zipfilesize)
    compression = round(totalfilesize / zipfilesize, 2)
    print(f'Compressed file is {compression}x smaller!')
    newZip.close()