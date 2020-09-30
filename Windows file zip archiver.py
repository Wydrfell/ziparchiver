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
def copy(src, dest):
    if os.path.isdir(dest):
        shutil.copy(src, dest)
    else:
        shutil.copy(src, dest)

   
#Set dest to src if dest is not given
dest = args.dest
src = args.src

if dest  == '':
    dest = src
    
if (not validpath(src, dest)):
    pass
else:
    pass
    #look at the options and sort accordingly

