import os
import sys
import glob

sDir = os.path.dirname(os.path.abspath(sys.argv[0]))
cwd = os.getcwd()
subDir = 'Songs'
songPath = os.path.join(cwd, subDir)
print(songPath)
print()

os.chdir(songPath)
for file in glob.glob("*.txt"):
    print(file)
