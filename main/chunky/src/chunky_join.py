import os

def join(path):
    if not os.path.exists(path):
        print(f"Path does not exist: {path}")
        exit(1)
    if not os.path.isdir(path):
        print(f"Path is not a directory: {path}")
        exit(1)

    meta_file = os.path.join(path, "meta")
    if not os.path.exists(meta_file):
        print("Meta file not found")
        exit(1)
    if not os.path.isfile(meta_file):
        print("Meta file invalid")
        exit(1)

    with open(meta_file, "r") as f:
        filename = f.read()
    new_file_path = os.path.join(os.getcwd(), filename)

    if os.path.exists(new_file_path):
        print(f"New file path already exists: {new_file_path}")
        exit(1)

    print("File info")
    print(f"New file name: {filename}")
    print(f"New file path: {new_file_path}")

    if input("Continue?") != "":
        print("Aborting")
        exit(1)

    print("Joining...")
    target = open(new_file_path, "wb")
    files = sorted([f.path for f in os.scandir(path) if not f.name == "meta"])
    for file in files:
        with open(file, "rb") as source:
            target.write(source.read())
    target.close()
    print("Done")
