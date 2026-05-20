with open("file.txt", "r") as f:
    for line in f:
        if "error" in line:
            print(line.strip())
        else:
            print("Nothing found")
