with open("file.txt", "r+") as f:
    content = f.read()
    f.write("appended at end")
