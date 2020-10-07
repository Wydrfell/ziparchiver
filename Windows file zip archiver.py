#Windows file archiver
import zipfile, os, shutil, argparse

# parse through arguments
parser = argparse.ArgumentParser(description='Archive and sort some files. List sort options in order by hierarchy.')
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

# Check to see if src and destination are valid directories

def validpath(*argv):
    for path in argv:
        path = os.path.abspath(path)
        if not(os.path.exists(path)):
            print(path, 'is not a valid directory or file.')
            return False
    return True

# copy file to target destination, or to the same directory as source file
# [REMOVE] dest is already processed to either having a value or defaulting to same 
# location as source file no need to branch off into two possibilities
def is_dir(path):
    if os.path.isdir(path):
        return True
    else:
        return False

def get_filename(path):
    i = len(path)
    while path[i-1] != "\\":
        i -= 1
    return path[i:]

def filetraverse(depth, filedir):

    for folderName, subfolder, files in os.walk(filedir):
        for files in folderName:
            fname = get_filename(files)
            #shutil.copy(src, dest)
def options():
    if args.day:
        # filetraverse
        # create copy foldername
        os.makedirs(dest, exist_ok = True)
        if not isfile:
            pass
            # filetraverse(1, src)
        else:
            zfile = zipfile.ZipFile(dest)

        print("Date Selected")

# Gives absolute path, returns current directory if path is empty string
dest = os.path.abspath(args.dest)
src = os.path.abspath(args.src)
print(f"These are the abspaths:\n{src}\n{dest}")

# check if src is a dir or a file
# If it is not a dir check to see if it is a file
if not os.path.isdir(src):
    print("The filename is:", get_filename(src))
    fname = get_filename(src)
    filedir = src.replace("\\" + fname, "")
    os.chdir(filedir)
    print("filedir:", filedir)
    print("join:", os.path.join(filedir,fname))
    if not os.path.isfile(fname):
        print(src, os.path.isfile(fname))
    else:
    # Set dest to filedir if dest is not given
        if dest  == '':
            dest = filedir

        # [REMOVE]    
        print(f"These are the directories:\n{filedir}\n{dest}")
        # options()
        if args.day:
            # filetraverse
            # create copy foldername
            os.makedirs(dest, exist_ok = True)
            zfile = zipfile.ZipFile(dest)

            print("Date Selected")

# if it is a dir
else:
    # Set dest to src if dest is not given
    if dest  == '':
        dest = src

    # [REMOVE]    
    print(f"These are the directories:\n{filedir}\n{dest}")