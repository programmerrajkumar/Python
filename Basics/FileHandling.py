import os

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

#w+ - read & write
#r+  - read write append
#a+ - read append

# t-text (default)
# b-binary
file = None
fileName = "filehandling.txt"
if not os.path.exists(fileName):
    f = open(fileName, "wt")
else:
    f = open(fileName, "wt")

f.write("""Line1
Line2
Line3
""")
f.close()

f = open(fileName, "r")
print(f.readline())  # reads line 1 and points to next line
f.close()

f = open(fileName, "at")
f.write("""
Line4
""")
f.close()
f = open(fileName, "r")
for line in f:
    print(line)

f.close()


