#Getting Full File Paths From a Directory and All Its Subdirectories

import os

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths("/Users/johnny/Desktop/TEST")


#You can use glob:

import glob, os
os.chdir("./mydir")
for file in glob.glob("*.txt"):
    print(file)
os.chdir("..")

#or simply os.listdir:

import os
for file in os.listdir("./mydir"):
    if file.endswith(".txt"):
        print(file)

#or if you want to traverse directory, use os.walk:

import os
for root, dirs, files in os.walk("./mydir"):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))


# another one
directory = "./mydir"
for root, dirs, files in os.walk(directory):
    print("root: {}".format(root))
    print("dirs: {}".format(dirs))
    print("files: {}".format(files))
    for file in files:
        if file.endswith('.txt'):
            print(file)

