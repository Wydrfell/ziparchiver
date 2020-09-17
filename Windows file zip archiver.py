#Windows file archiver
import zipfile, os, shutil

def main():
    src = input("Please enter the complete file extension or folder of where/what you want to archive:\n")
    dest = input("Enter the desired destination for the zipped file, leave empty if destination is the same locationas the source:\n")
   
    #Set dest to src if dest is not given
    if dest  == '':
        dest = src
    
    validpath(src, dest)

    # check for user options 
    # Will be using a series of input() functions to grab user input for options in lieu of a proper GUI
    # may consider just using flags in the future 
    
#Check to see if src and destination are valid directories
def validpath(*argv):
    for path in argv:
        path = os.path.abspath(path)
        if not(os.path.exists(path)):
            print(path, 'is not a valid directory or file.')
            break
            
def useroptions():

    # Allows users some options to how the files are archived
    print('Select the sorting type in order from highest level to lowest. Each flag can only be used once')
    flags = input('d: sort by date (day); m: sort by year and month; t: sort by file type; f: by folder; a: alphanumeric; s: size; n: none (or zip as is); h or help: help')
    if 'n' in flags:
        flags = 'n'
    elif 'h' in flags:
        print('An example would be: mdt which would first sort the files into folders labeled by the year and month, then inside these folder there are folders labeling the days and lastly inside the date folders there will be folders sorting the files by file type. ')

    else:
        options = len(flags)
    
    for opt in flags:
        pass

     
    

if __name__ == '__main__':
    main()