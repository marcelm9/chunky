import os

def split(path, max_chunk_size):
    if not os.path.exists(path):
        print(f"Path does not exist: {path}")
        exit(1)
    if not os.path.isfile(path):
        print(f"Path is not a file: {path}")
        exit(1)
    if max_chunk_size < 5:
        print("Min size for chunks is 5")
        exit(1)
    elif max_chunk_size > 500:
        print("Max size for chunks is 500")
        exit(1)

    # print info about file
    size_precise = os.path.getsize(path)
    size_in_mb = round(size_precise / 1_000_000, 2)
    if size_in_mb < max_chunk_size:
        print(f"File is smaller than chunk size ({size_in_mb} < {max_chunk_size})")
        exit(1)

    filename = os.path.basename(path)
    chunk_count = int(size_in_mb / max_chunk_size) + 1
    chunk_size = round(size_in_mb / chunk_count, 2)
    chunk_sizes_precise = [int(size_precise / chunk_count) for i in range(chunk_count)]
    chunk_sizes_precise[-1] += size_precise % chunk_count
    new_folder = os.path.join(os.path.dirname(path), "chunks")

    print("File info")
    print(f"File name:  {filename}")
    print(f"Path:       {path}")
    print(f"Size:       {size_in_mb} MB")
    print(f"Chunks:     {chunk_count}")
    print(f"Chunk size: {chunk_size} MB")
    print(f"New folder: {new_folder}")

    if input("Continue?") != "":
        print("Aborting")
        exit(1)

    print("Starting...")
    source = open(path, "rb")
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    # writing meta file
    meta_file_path = os.path.join(new_folder, "meta")
    with open(meta_file_path, "w") as f:
        f.write(filename)

    # copying content
    new_files = [f"chunk{i}" for i in range(chunk_count)]
    for i in range(chunk_count):
        with open(os.path.join(new_folder, new_files[i]), "wb") as target:
            target.write(source.read(chunk_sizes_precise[i]))
    print("Done")
