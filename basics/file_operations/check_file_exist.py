import os
if os.path.exists("file.txt"):
    with open("file.txt", "r") as f:
        print(f.read())
else:
    print("File not found")
