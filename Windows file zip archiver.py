#Windows file archiver
import zipfile, os, shutil, argparse, sys

class ArgumentError(Exception):

    def __init__(self,path):
        self.path = path

    def __str__(self):
        return(repr(self.path))

def directoryZip(src, dest):
    pass

def getFilename(path):
    i = len(path)
    while path[i-1] != "\\":
        i -= 1
    return path[i:]

    print(f"These are the abspaths:\n{src}\n{dest}")

def setDest(src, dest):
    if dest == '':
        fname = getFilename(src)
        filedir = src.replace("\\" + fname, "")
        return(os.path.abspath(filedir))
    else:
        return(os.path.abspath(dest))

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
        src = src = os.path.abspath(args.src)
        dest = setDest(src, args.dest)
        directoryZip(src, dest)
else:
    print("File Detected.")
    print("Zipping File...")
    src = os.path.abspath(args.src)
    dest = setDest(src, args.dest)
    newZip = zipfile.ZipFile(zipname, 'w')
    newZip.write(src, compress_type=zipfile.ZIP_DEFLATED)
    print(newZip.namelist())
    zipInfo = newZip.getinfo(newZip.namelist()[0])
    totalfilesize += zipInfo.file_size
    zipfilesize += zipInfo.compress_size
    print("og file:", totalfilesize, "\ncompressed:", zipfilesize)
    compression = round(totalfilesize / zipfilesize, 2)
    print(f'Compressed file is {compression}x smaller!')
    newZip.close()