#Windows file archiver
import zipfile, os, shutil

def main():
    src = input("Please enter the complete file extension or folder of where/what you want to archive:\n")
    dest = input("Enter the desired destination for the zipped file, leave empty if destination is the same locationas the source:\n")
   
    #Set dest to src if dest is not given
    if dest  == '':
        dest = src
    
    validpath(src, dest)
    
#Check to see if src and destination are valid directories
def validpath(*argv):
    for path in argv:
        path = os.path.abspath(path)
        if not(os.path.exists(path)):
            print(path, 'is not a valid directory or file.')
            break
            

if __name__ == '__main__':
    main()


