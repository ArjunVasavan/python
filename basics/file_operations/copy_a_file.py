with open("file.txt", "r") as src:
    with open("dest.txt", "w") as dst:
        dst.write(src.read())
