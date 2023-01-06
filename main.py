from Database import *
from Load import *
from Transform import *
import os, glob

def cleanFilesFolder(path_files_folder="./files"):
    files = glob.glob(path_files_folder + "/*")
    for f in files:
        os.remove(f)

    

if __name__ == "__main__":
    db = Database()

    # Extract

    # Transform

    # Load
    load = Load()
    load.send_all_files()
    

